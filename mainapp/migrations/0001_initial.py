# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Main'
        db.create_table(u'mainapp_main', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')
             (max_length=75)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mainapp', ['Main'])

    def backwards(self, orm):
        # Deleting model 'Main'
        db.delete_table(u'mainapp_main')

    models = {
        u'mainapp.main': {
            'Meta': {'object_name': 'Main'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})

        }
    }

    complete_apps = ['mainapp']