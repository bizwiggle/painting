# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Why_Us'
        db.create_table(u'pages_why_us', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('reason1', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason1_blurb', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('reason1_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('reason2', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason2_blurb', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('reason2_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('reason3', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason3_blurb', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('reason3_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('reason4', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason4_blurb', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('reason4_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('reason5', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason5_blurb', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('reason5_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Why_Us'])


    def backwards(self, orm):
        # Deleting model 'Why_Us'
        db.delete_table(u'pages_why_us')


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
            'has_comercial_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_other_services_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_residential_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 13, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'linkedin_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'logo': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo_small': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        u'pages.services': {
            'Meta': {'object_name': 'Services'},
            'comercial_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'comercial_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_services_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'other_services_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'residential_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'residential_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'service_area_blurb': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list10': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list10_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list1_link': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'service_list2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list2_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list3': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list3_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list4': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list4_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list5': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list5_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list6': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list6_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list7': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list7_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list8': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list8_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list9': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list9_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.success_stories': {
            'Meta': {'object_name': 'Success_Stories'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'story1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'story1_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'story1_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'story2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'story2_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'story2_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'story3': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'story3_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'story3_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.why_us': {
            'Meta': {'object_name': 'Why_Us'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason1': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason1_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'reason1_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason2': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason2_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'reason2_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason3': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason3_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'reason3_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason4': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason4_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'reason4_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason5': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason5_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'reason5_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pages']