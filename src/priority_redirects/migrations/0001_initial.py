# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Redirect'
        db.create_table('django_redirect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('old_path', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('new_path', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'priority_redirects', ['Redirect'])

        # Adding unique constraint on 'Redirect', fields ['site', 'old_path']
        db.create_unique('django_redirect', ['site_id', 'old_path'])


    def backwards(self, orm):
        # Removing unique constraint on 'Redirect', fields ['site', 'old_path']
        db.delete_unique('django_redirect', ['site_id', 'old_path'])

        # Deleting model 'Redirect'
        db.delete_table('django_redirect')


    models = {
        u'priority_redirects.redirect': {
            'Meta': {'ordering': "('old_path',)", 'unique_together': "(('site', 'old_path'),)", 'object_name': 'Redirect', 'db_table': "'django_redirect'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'old_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['priority_redirects']