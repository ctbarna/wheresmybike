from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

from rest_framework import routers

from finder.views import BaseView, CityViewSet

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', BaseView.as_view()),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/v1/', include(router.urls)),
        #url(r'^(?P<slug>.+)/', StationListView.as_view()),
)
