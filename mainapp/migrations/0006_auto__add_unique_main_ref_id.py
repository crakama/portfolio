# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Main', fields ['ref_id']
        db.create_unique(u'mainapp_main', ['ref_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Main', fields ['ref_id']
        db.delete_unique(u'mainapp_main', ['ref_id'])


    models = {
        u'mainapp.main': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Main'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'IPAddress'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ReferenceID'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mainapp']