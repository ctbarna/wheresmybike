from django.contrib.gis import admin
from .models import City, Station

class CityAdmin(admin.GeoModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(City, CityAdmin)
admin.site.register(Station, admin.GeoModelAdmin)
