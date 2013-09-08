from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.gis.geos import GEOSGeometry

from rest_framework import viewsets, generics as rest_generics
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .models import City, Station
from .serializers import CitySerializer, StationSerializer

class BaseView(TemplateView):
    template_name = "app.html"

class StationListView(rest_generics.ListAPIView):
    serializer_class = StationSerializer

    def get_queryset(self):
        city = get_object_or_404(City, slug=self.kwargs["city"])
        return Station.objects.filter(city=city)

class LatLonAPIException(APIException):
    status_code = 400
    detail = "lat and lon are required parameters."

class ClosestStationView(rest_generics.RetrieveAPIView):
    serializer_class = StationSerializer

    def get_object(self):
        city = get_object_or_404(City, slug=self.kwargs["city"])
        lat = self.request.QUERY_PARAMS.get('lat', None)
        lon = self.request.QUERY_PARAMS.get('lon', None)

        if not lat and not lon:
            raise LatLonAPIException

        location = GEOSGeometry("POINT(%s %s)" % (lon, lat))

        return Station.objects.distance(location).filter(city=city,
                bikes__gt=0).order_by("distance")[0]
