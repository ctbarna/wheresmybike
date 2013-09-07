# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'finder_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('sync_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'finder', ['City'])

        # Adding model 'Station'
        db.create_table(u'finder_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('terminal_name', self.gf('django.db.models.fields.IntegerField')()),
            ('last_com_with_server', self.gf('django.db.models.fields.DateTimeField')()),
            ('coords', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('install_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('removal_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('installed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('locked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('temporary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bikes', self.gf('django.db.models.fields.IntegerField')()),
            ('empty_docks', self.gf('django.db.models.fields.IntegerField')()),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finder.City'])),
        ))
        db.send_create_signal(u'finder', ['Station'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'finder_city')

        # Deleting model 'Station'
        db.delete_table(u'finder_station')


    models = {
        u'finder.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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