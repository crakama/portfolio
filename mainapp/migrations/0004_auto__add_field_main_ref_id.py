# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Main.ref_id'
        db.add_column(u'mainapp_main', 'ref_id',
                      self.gf('django.db.models.fields.CharField')(default='ReferenceID', max_length=120),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Main.ref_id'
        db.delete_column(u'mainapp_main', 'ref_id')


    models = {
        u'mainapp.main': {
            'Meta': {'object_name': 'Main'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'IPAddress'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ReferenceID'", 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mainapp']