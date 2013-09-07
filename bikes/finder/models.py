from django.contrib.gis.db import models
from timezone_field import TimeZoneField

class City(models.Model):
    name = models.CharField(max_length="255")
    slug = models.SlugField()
    timezone = TimeZoneField(default="America/New_York")
    sync_url = models.URLField()
    last_synced = models.DateTimeField(null=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"


class Station(models.Model):
    name = models.CharField(max_length="255")
    terminal_name = models.IntegerField()
    last_com_with_server = models.DateTimeField()
    coordinates = models.PointField(srid=4326)

    install_date = models.DateTimeField(null=True)
    removal_date = models.DateTimeField(null=True)

    installed = models.BooleanField()
    locked = models.BooleanField()
    temporary = models.BooleanField()
    public = models.BooleanField()

    bikes = models.IntegerField()
    empty_docks = models.IntegerField()

    last_updated = models.DateTimeField(null=True)

    city = models.ForeignKey(City, related_name="stations")

    # Custom Manager
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.city)
