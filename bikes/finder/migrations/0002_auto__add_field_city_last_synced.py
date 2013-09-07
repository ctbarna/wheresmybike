# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'City.last_synced'
        db.add_column(u'finder_city', 'last_synced',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'City.last_synced'
        db.delete_column(u'finder_city', 'last_synced')


    models = {
        u'finder.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_synced': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sync_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'finder.station': {
            'Meta': {'object_name': 'Station'},
            'bikes': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finder.City']"}),
            'coords': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'empty_docks': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install_date': ('django.db.models.fields.DateTimeField', [], {}),
            'installed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_com_with_server': ('django.db.models.fields.DateTimeField', [], {}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'removal_date': ('django.db.models.fields.DateTimeField', [], {}),
            'temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'terminal_name': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['finder']