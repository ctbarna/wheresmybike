from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.response import Response

from .models import City, Station
from .serializers import CitySerializer

class BaseView(TemplateView):
    template_name = "app.html"

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
