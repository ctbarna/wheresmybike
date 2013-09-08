from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

from finder.views import BaseView, ClosestStationView, \
    StationListView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', BaseView.as_view()),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/v1/(?P<city>.+)/nearest/', ClosestStationView.as_view()),
        url(r'^api/v1/(?P<city>.+)/', StationListView.as_view()),
)
