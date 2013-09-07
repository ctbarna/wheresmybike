# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Station.coords'
        db.delete_column(u'finder_station', 'coords')

        # Adding field 'Station.coordinates'
        db.add_column(u'finder_station', 'coordinates',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(default='POINT(0 0)'),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Station.coords'
        raise RuntimeError("Cannot reverse this migration. 'Station.coords' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Station.coords'
        db.add_column(u'finder_station', 'coords',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(),
                      keep_default=False)

        # Deleting field 'Station.coordinates'
        db.delete_column(u'finder_station', 'coordinates')


    models = {
        u'finder.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_synced': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sync_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'timezone': ('timezone_field.fields.TimeZoneField', [], {'default': "'America/New_York'"})
        },
        u'finder.station': {
            'Meta': {'object_name': 'Station'},
            'bikes': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations'", 'to': u"orm['finder.City']"}),
            'coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'empty_docks': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'installed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_com_with_server': ('django.db.models.fields.DateTimeField', [], {}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'removal_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'terminal_name': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['finder']