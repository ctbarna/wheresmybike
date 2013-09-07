from datetime import datetime
from optparse import make_option
from xml.etree import ElementTree

from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.gis.geos import Point

from pytz import timezone
import requests

from finder.models import City, Station

def handle_date(data, city=None):
    if data is None:
        return None
    return datetime.fromtimestamp(int(data) / 1000, city.timezone)

def handle_bool(data, city=None):
    return data.lower() == "true"

def handle_point(data, city=None):
    return Point([float(coord) for coord in data])

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
            make_option("--all",
                action="store_true",
                dest="all",
                default=False,
                help="Force all stations to refresh."),
            )

    field_mappings = {
        "name": ("name", str,),
        "terminal_name": ("terminalName", int,),
        "last_com_with_server": ("lastCommWithServer", handle_date,),
        "coordinates": (("long", "lat"), handle_point,),
        "install_date": ("installDate", handle_date,),
        "removal_date": ("removaleDate", handle_date,),
        "installed": ("installed", handle_bool,),
        "locked": ("locked", handle_bool,),
        "temporary": ("temporary", handle_bool,),
        "public": ("public", handle_bool,),
        "bikes": ("nbBikes", int,),
        "empty_docks": ("nbEmptyDocks", int,),
        "last_updated": ("latestUpdateTime", handle_date,),
    }

    def handle(self, *args, **options):
        cities = City.objects.all()

        for city in cities:
            self.stdout.write("Syncing %s." % city)
            data = requests.get(city.sync_url)
            stations = ElementTree.fromstring(data.content)

            for station in stations.iter("station"):
                clean_station, created = self._parseStation(station, city)
                if not clean_station.last_updated or \
                        options["all"] or \
                        clean_station.last_updated > city.last_synced:
                    clean_station.save()

                    verb = "Created" if created else "Updated"
                    self.stdout.write("%s: %s" % (verb, str(clean_station)))

            city.last_synced = datetime.now(timezone(settings.TIME_ZONE))
            city.save()

    def _parseStation(self, station, city):
        station_id = int(station.find("terminalName").text)
        station_obj, created = Station.objects.get_or_create(city=city, terminal_name=station_id)

        for key, value in self.field_mappings.iteritems():
            if isinstance(value[0], basestring):
                tree_elem = station.find(value[0])
                if tree_elem is None:
                    continue
                tree_val = tree_elem.text
            else:
                tree_val = [station.find(val).text for val in value[0]]

            if value[1] is handle_date:
                clean_val = value[1](tree_val, city)
            else:
                clean_val = value[1](tree_val)

            if clean_val is not None:
                setattr(station_obj, key, clean_val)

        return (station_obj, created)
