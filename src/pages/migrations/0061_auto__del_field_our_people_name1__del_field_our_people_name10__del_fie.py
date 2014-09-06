# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Our_People.name1'
        db.delete_column(u'pages_our_people', 'name1')

        # Deleting field 'Our_People.name10'
        db.delete_column(u'pages_our_people', 'name10')

        # Deleting field 'Our_People.name6'
        db.delete_column(u'pages_our_people', 'name6')

        # Deleting field 'Our_People.name7'
        db.delete_column(u'pages_our_people', 'name7')

        # Deleting field 'Our_People.name4'
        db.delete_column(u'pages_our_people', 'name4')

        # Deleting field 'Our_People.name5'
        db.delete_column(u'pages_our_people', 'name5')

        # Deleting field 'Our_People.name2'
        db.delete_column(u'pages_our_people', 'name2')

        # Deleting field 'Our_People.name3'
        db.delete_column(u'pages_our_people', 'name3')

        # Deleting field 'Our_People.name8'
        db.delete_column(u'pages_our_people', 'name8')

        # Deleting field 'Our_People.name9'
        db.delete_column(u'pages_our_people', 'name9')

        # Deleting field 'Our_People.person_title5'
        db.delete_column(u'pages_our_people', 'person_title5')

        # Deleting field 'Our_People.person_title4'
        db.delete_column(u'pages_our_people', 'person_title4')

        # Deleting field 'Our_People.person_title7'
        db.delete_column(u'pages_our_people', 'person_title7')

        # Deleting field 'Our_People.person_title6'
        db.delete_column(u'pages_our_people', 'person_title6')

        # Deleting field 'Our_People.person_title1'
        db.delete_column(u'pages_our_people', 'person_title1')

        # Deleting field 'Our_People.person_title3'
        db.delete_column(u'pages_our_people', 'person_title3')

        # Deleting field 'Our_People.person_title2'
        db.delete_column(u'pages_our_people', 'person_title2')

        # Deleting field 'Our_People.person_title9'
        db.delete_column(u'pages_our_people', 'person_title9')

        # Deleting field 'Our_People.person_title10'
        db.delete_column(u'pages_our_people', 'person_title10')

        # Adding field 'Our_People.title1'
        db.add_column(u'pages_our_people', 'title1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title2'
        db.add_column(u'pages_our_people', 'title2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title3'
        db.add_column(u'pages_our_people', 'title3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title4'
        db.add_column(u'pages_our_people', 'title4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title5'
        db.add_column(u'pages_our_people', 'title5',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title6'
        db.add_column(u'pages_our_people', 'title6',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title7'
        db.add_column(u'pages_our_people', 'title7',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title8'
        db.add_column(u'pages_our_people', 'title8',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title9'
        db.add_column(u'pages_our_people', 'title9',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.title10'
        db.add_column(u'pages_our_people', 'title10',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Our_People.name1'
        db.add_column(u'pages_our_people', 'name1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name10'
        db.add_column(u'pages_our_people', 'name10',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name6'
        db.add_column(u'pages_our_people', 'name6',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name7'
        db.add_column(u'pages_our_people', 'name7',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name4'
        db.add_column(u'pages_our_people', 'name4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name5'
        db.add_column(u'pages_our_people', 'name5',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name2'
        db.add_column(u'pages_our_people', 'name2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name3'
        db.add_column(u'pages_our_people', 'name3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name8'
        db.add_column(u'pages_our_people', 'name8',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.name9'
        db.add_column(u'pages_our_people', 'name9',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title5'
        db.add_column(u'pages_our_people', 'person_title5',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title4'
        db.add_column(u'pages_our_people', 'person_title4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title7'
        db.add_column(u'pages_our_people', 'person_title7',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title6'
        db.add_column(u'pages_our_people', 'person_title6',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title1'
        db.add_column(u'pages_our_people', 'person_title1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title3'
        db.add_column(u'pages_our_people', 'person_title3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title2'
        db.add_column(u'pages_our_people', 'person_title2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title9'
        db.add_column(u'pages_our_people', 'person_title9',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Adding field 'Our_People.person_title10'
        db.add_column(u'pages_our_people', 'person_title10',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=48, blank=True),
                      keep_default=False)

        # Deleting field 'Our_People.title1'
        db.delete_column(u'pages_our_people', 'title1')

        # Deleting field 'Our_People.title2'
        db.delete_column(u'pages_our_people', 'title2')

        # Deleting field 'Our_People.title3'
        db.delete_column(u'pages_our_people', 'title3')

        # Deleting field 'Our_People.title4'
        db.delete_column(u'pages_our_people', 'title4')

        # Deleting field 'Our_People.title5'
        db.delete_column(u'pages_our_people', 'title5')

        # Deleting field 'Our_People.title6'
        db.delete_column(u'pages_our_people', 'title6')

        # Deleting field 'Our_People.title7'
        db.delete_column(u'pages_our_people', 'title7')

        # Deleting field 'Our_People.title8'
        db.delete_column(u'pages_our_people', 'title8')

        # Deleting field 'Our_People.title9'
        db.delete_column(u'pages_our_people', 'title9')

        # Deleting field 'Our_People.title10'
        db.delete_column(u'pages_our_people', 'title10')


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
        u'pages.about': {
            'Meta': {'object_name': 'About'},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'info2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'info3': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'info4': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'info5': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'info_headline': ('django.db.models.fields.CharField', [], {'default': "'The Bottom Line'", 'max_length': '32', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.comercial_service': {
            'Meta': {'object_name': 'Comercial_Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'paragraph1': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'paragraph2': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'paragraph3': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'paragraph_headline1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'paragraph_headline2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'paragraph_headline3': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'pic1': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic2': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic3': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.general_info': {
            'Meta': {'object_name': 'General_Info'},
            'banner_text': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'business_name': ('django.db.models.fields.CharField', [], {'default': "'Business Name'", 'max_length': '64', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '64', 'blank': 'True'}),
            'contact_meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'}),
            'extra_address': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'facebook_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '17', 'blank': 'True'}),
            'google_plus_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'has_comercial_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_other_services_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_residential_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'linkedin_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'logo': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo_small': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '17', 'blank': 'True'}),
            'pintrest_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'portfolio_meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '2', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'tumblr_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"}),
            'why_us_brief': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'pages.index': {
            'Meta': {'object_name': 'Index'},
            'about_blurb': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'affilation_pic1': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'affilation_pic2': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'affilation_pic3': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'affilation_pic4': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'affilation_pic5': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'affilation_pic6': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hello_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hello_title': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'hello_txt': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slider_link1': ('django.db.models.fields.CharField', [], {'default': "'Contact'", 'max_length': '30', 'blank': 'True'}),
            'slider_link2': ('django.db.models.fields.CharField', [], {'default': "'Contact'", 'max_length': '30', 'blank': 'True'}),
            'slider_link3': ('django.db.models.fields.CharField', [], {'default': "'Contact'", 'max_length': '30', 'blank': 'True'}),
            'slider_link4': ('django.db.models.fields.CharField', [], {'default': "'Contact'", 'max_length': '30', 'blank': 'True'}),
            'slider_link5': ('django.db.models.fields.CharField', [], {'default': "'Contact'", 'max_length': '30', 'blank': 'True'}),
            'slider_txt_bottom1': ('django.db.models.fields.CharField', [], {'default': "'Hassle Free Estimate'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_bottom2': ('django.db.models.fields.CharField', [], {'default': "'Hassle Free Estimate'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_bottom3': ('django.db.models.fields.CharField', [], {'default': "'Hassle Free Estimate'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_bottom4': ('django.db.models.fields.CharField', [], {'default': "'Hassle Free Estimate'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_bottom5': ('django.db.models.fields.CharField', [], {'default': "'Hassle Free Estimate'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_top1': ('django.db.models.fields.CharField', [], {'default': "'Request a'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_top2': ('django.db.models.fields.CharField', [], {'default': "'Request a'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_top3': ('django.db.models.fields.CharField', [], {'default': "'Request a'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_top4': ('django.db.models.fields.CharField', [], {'default': "'Request a'", 'max_length': '32', 'blank': 'True'}),
            'slider_txt_top5': ('django.db.models.fields.CharField', [], {'default': "'Request a'", 'max_length': '32', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"}),
            'why_us_blurb': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'})
        },
        u'pages.other_services': {
            'Meta': {'object_name': 'Other_Services'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'pic1': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic2': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic3': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic4': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic5': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'service1': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'service2': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'service3': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'service4': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'service5': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'service_headline1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_headline2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_headline3': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_headline4': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_headline5': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.our_people': {
            'Meta': {'object_name': 'Our_People'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'person_title8': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'pic1': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic10': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic2': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic3': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic4': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic5': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic6': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic7': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic8': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic9': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'text1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text10': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text3': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text4': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text5': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text6': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text7': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text8': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'text9': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'title1': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title10': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title2': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title3': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title4': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title5': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title6': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title7': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title8': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'title9': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.portfolio_pic': {
            'Meta': {'object_name': 'Portfolio_Pic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'thumb': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.residential_service': {
            'Meta': {'object_name': 'Residential_Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'paragraph1': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'paragraph2': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'paragraph3': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'paragraph_headline1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'paragraph_headline2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'paragraph_headline3': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'pic1': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic2': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic3': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.services': {
            'Meta': {'object_name': 'Services'},
            'comercial_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'comercial_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'other_services_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'other_services_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'residential_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'residential_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'service_area_blurb': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list10': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'service_list10_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
            'service_list1_link': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'other_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 5, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'reason1': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason1_blurb': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'reason1_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason2': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason2_blurb': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'reason2_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason3': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason3_blurb': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'reason3_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason4': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason4_blurb': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'reason4_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason5': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'reason5_blurb': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
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