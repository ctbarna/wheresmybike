from finder.models import City, Station

from rest_framework import serializers

class PointField(serializers.Field):
    def to_native(self, obj):
        return [obj.y, obj.x]

class StationSerializer(serializers.HyperlinkedModelSerializer):
    coordinates = PointField(source='coordinates')
    class Meta:
        model = Station
        fields = ('name', 'coordinates', 'bikes', 'empty_docks',)

class CitySerializer(serializers.HyperlinkedModelSerializer):
    stations = StationSerializer(many=True)
    class Meta:
        model = City
        fields = ('name', 'url', 'stations',)
