# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Social'
        db.delete_table(u'pages_social')

        # Adding field 'General_Info.facebook_URL'
        db.add_column(u'pages_general_info', 'facebook_URL',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'General_Info.linkedin_URL'
        db.add_column(u'pages_general_info', 'linkedin_URL',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'General_Info.google_plus_URL'
        db.add_column(u'pages_general_info', 'google_plus_URL',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'General_Info.twitter_URL'
        db.add_column(u'pages_general_info', 'twitter_URL',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'General_Info.tumblr_URL'
        db.add_column(u'pages_general_info', 'tumblr_URL',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'General_Info.pintrest_URL'
        db.add_column(u'pages_general_info', 'pintrest_URL',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Social'
        db.create_table(u'pages_social', (
            ('pintrest_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('tumblr_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('facebook_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('linkedin_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('google_plus_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'pages', ['Social'])

        # Deleting field 'General_Info.facebook_URL'
        db.delete_column(u'pages_general_info', 'facebook_URL')

        # Deleting field 'General_Info.linkedin_URL'
        db.delete_column(u'pages_general_info', 'linkedin_URL')

        # Deleting field 'General_Info.google_plus_URL'
        db.delete_column(u'pages_general_info', 'google_plus_URL')

        # Deleting field 'General_Info.twitter_URL'
        db.delete_column(u'pages_general_info', 'twitter_URL')

        # Deleting field 'General_Info.tumblr_URL'
        db.delete_column(u'pages_general_info', 'tumblr_URL')

        # Deleting field 'General_Info.pintrest_URL'
        db.delete_column(u'pages_general_info', 'pintrest_URL')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pages.general_info': {
            'Meta': {'object_name': 'General_Info'},
            'banner_text': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'business_name': ('django.db.models.fields.CharField', [], {'default': "'Business Name'", 'max_length': '64', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'}),
            'extra_address': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'facebook_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '17', 'blank': 'True'}),
            'google_plus_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 11, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'linkedin_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'logo_small': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '17', 'blank': 'True'}),
            'pintrest_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '2', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'tumblr_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"}),
            'why_us_brief': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pages']