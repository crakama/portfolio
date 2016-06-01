# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Main.friend_invite'
        db.delete_column(u'mainapp_main', 'friend_invite_id')

        # Adding field 'Main.reffered_by'
        db.add_column(u'mainapp_main', 'reffered_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='referral', null=True, to=orm['mainapp.Main']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Main.friend_invite'
        db.add_column(u'mainapp_main', 'friend_invite',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='referral', null=True, to=orm['mainapp.Main'], blank=True),
                      keep_default=False)

        # Deleting field 'Main.reffered_by'
        db.delete_column(u'mainapp_main', 'reffered_by_id')


    models = {
        u'mainapp.main': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Main'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'IPAddress'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ReferenceID'", 'unique': 'True', 'max_length': '120'}),
            'reffered_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referral'", 'null': 'True', 'to': u"orm['mainapp.Main']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mainapp']