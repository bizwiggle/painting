# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'General_Info'
        db.create_table(u'pages_general_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('business_name', self.gf('django.db.models.fields.CharField')(default='Your Business Name', max_length=64, blank=True)),
            ('has_residential_page', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('has_comercial_page', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('has_other_services_page', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('logo', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('logo_small', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(db_index=True, max_length=75, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('extra_address', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=64, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=2, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=5, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=17, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=17, blank=True)),
            ('why_us_brief', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('banner_text', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('facebook_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('linkedin_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('google_plus_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('tumblr_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pintrest_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('contact_meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('portfolio_meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('meta_title', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('is_website_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['General_Info'])

        # Adding model 'Index'
        db.create_table(u'pages_index', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('slider_txt_top1', self.gf('django.db.models.fields.CharField')(default='Request a', max_length=32, blank=True)),
            ('slider_txt_bottom1', self.gf('django.db.models.fields.CharField')(default='Hassle Free Estimate', max_length=32, blank=True)),
            ('slider_link1', self.gf('django.db.models.fields.CharField')(default='H', max_length=30, blank=True)),
            ('slider_txt_top2', self.gf('django.db.models.fields.CharField')(default='Request a', max_length=32, blank=True)),
            ('slider_txt_bottom2', self.gf('django.db.models.fields.CharField')(default='Hassle Free Estimate', max_length=32, blank=True)),
            ('slider_link2', self.gf('django.db.models.fields.CharField')(default='H', max_length=30, blank=True)),
            ('slider_txt_top3', self.gf('django.db.models.fields.CharField')(default='Request a', max_length=32, blank=True)),
            ('slider_txt_bottom3', self.gf('django.db.models.fields.CharField')(default='Hassle Free Estimate', max_length=32, blank=True)),
            ('slider_link3', self.gf('django.db.models.fields.CharField')(default='H', max_length=30, blank=True)),
            ('slider_txt_top4', self.gf('django.db.models.fields.CharField')(default='Request a', max_length=32, blank=True)),
            ('slider_txt_bottom4', self.gf('django.db.models.fields.CharField')(default='Hassle Free Estimate', max_length=32, blank=True)),
            ('slider_link4', self.gf('django.db.models.fields.CharField')(default='H', max_length=30, blank=True)),
            ('slider_txt_top5', self.gf('django.db.models.fields.CharField')(default='Request a', max_length=32, blank=True)),
            ('slider_txt_bottom5', self.gf('django.db.models.fields.CharField')(default='Hassle Free Estimate', max_length=32, blank=True)),
            ('slider_link5', self.gf('django.db.models.fields.CharField')(default='H', max_length=30, blank=True)),
            ('slider_pic', self.gf('django.db.models.fields.CharField')(default='PG', max_length=2, blank=True)),
            ('why_us_blurb', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('about_blurb', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('hello_title', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('hello_txt', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('hello_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('affilation_pic1', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('affilation1_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('affilation_pic2', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('affilation2_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('affilation_pic3', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('affilation3_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('affilation_pic4', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('affilation4_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('affilation_pic5', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('affilation5_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('affilation_pic6', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('affilation6_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Index'])

        # Adding model 'Success_Stories'
        db.create_table(u'pages_success_stories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('story1', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('story1_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('story1_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('story2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('story2_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('story2_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('story3', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('story3_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('story3_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('other_URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Success_Stories'])

        # Adding model 'Services'
        db.create_table(u'pages_services', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('residential_blurb', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('residential_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('comercial_blurb', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('comercial_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('other_services_blurb', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('other_services_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('service_area_blurb', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('service_list1', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list1_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list2', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list2_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list3', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list3_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list4', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list4_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list5', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list5_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list6', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list6_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list7', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list7_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list8', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list8_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list9', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list9_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('service_list10', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service_list10_link', self.gf('django.db.models.fields.CharField')(default='N', max_length=1, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Services'])

        # Adding model 'Residential_Service'
        db.create_table(u'pages_residential_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('pic1', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic2', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic3', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('paragraph_headline1', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('paragraph1', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('paragraph_headline2', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('paragraph2', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('paragraph_headline3', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('paragraph3', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Residential_Service'])

        # Adding model 'Comercial_Service'
        db.create_table(u'pages_comercial_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('pic1', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic2', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic3', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('paragraph_headline1', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('paragraph1', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('paragraph_headline2', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('paragraph2', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('paragraph_headline3', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('paragraph3', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Comercial_Service'])

        # Adding model 'Other_Services'
        db.create_table(u'pages_other_services', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('pic1', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic2', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic3', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic4', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic5', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('service_headline1', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service1', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('service_headline2', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service2', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('service_headline3', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service3', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('service_headline4', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service4', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('service_headline5', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('service5', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Other_Services'])

        # Adding model 'Why_Us'
        db.create_table(u'pages_why_us', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('reason1', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason1_blurb', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
            ('reason1_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('reason2', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason2_blurb', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
            ('reason2_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('reason3', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason3_blurb', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
            ('reason3_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('reason4', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason4_blurb', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
            ('reason4_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('reason5', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('reason5_blurb', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
            ('reason5_pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Why_Us'])

        # Adding model 'Portfolio_Pic'
        db.create_table(u'pages_portfolio_pic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('thumb', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('pic_type', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Portfolio_Pic'])

        # Adding model 'About'
        db.create_table(u'pages_about', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('pic', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('info_headline', self.gf('django.db.models.fields.CharField')(default='The Bottom Line', max_length=32, blank=True)),
            ('info1', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('info2', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('info3', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('info4', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('info5', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['About'])

        # Adding model 'Our_People'
        db.create_table(u'pages_our_people', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title1', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text1', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic1', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title2', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic2', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title3', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text3', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic3', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title4', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text4', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic4', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title5', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text5', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic5', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title6', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text6', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic6', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title7', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text7', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic7', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title8', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text8', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic8', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title9', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text9', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic9', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('title10', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('text10', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('pic10', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 21, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Our_People'])


    def backwards(self, orm):
        # Deleting model 'General_Info'
        db.delete_table(u'pages_general_info')

        # Deleting model 'Index'
        db.delete_table(u'pages_index')

        # Deleting model 'Success_Stories'
        db.delete_table(u'pages_success_stories')

        # Deleting model 'Services'
        db.delete_table(u'pages_services')

        # Deleting model 'Residential_Service'
        db.delete_table(u'pages_residential_service')

        # Deleting model 'Comercial_Service'
        db.delete_table(u'pages_comercial_service')

        # Deleting model 'Other_Services'
        db.delete_table(u'pages_other_services')

        # Deleting model 'Why_Us'
        db.delete_table(u'pages_why_us')

        # Deleting model 'Portfolio_Pic'
        db.delete_table(u'pages_portfolio_pic')

        # Deleting model 'About'
        db.delete_table(u'pages_about')

        # Deleting model 'Our_People'
        db.delete_table(u'pages_our_people')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'check_stripe_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.comercial_service': {
            'Meta': {'object_name': 'Comercial_Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
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
            'business_name': ('django.db.models.fields.CharField', [], {'default': "'Your Business Name'", 'max_length': '64', 'blank': 'True'}),
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
            'is_website_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'linkedin_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'logo': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo_small': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'meta_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
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
            'affilation1_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'affilation2_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'affilation3_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'affilation4_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'affilation5_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'affilation6_URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slider_link1': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '30', 'blank': 'True'}),
            'slider_link2': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '30', 'blank': 'True'}),
            'slider_link3': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '30', 'blank': 'True'}),
            'slider_link4': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '30', 'blank': 'True'}),
            'slider_link5': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '30', 'blank': 'True'}),
            'slider_pic': ('django.db.models.fields.CharField', [], {'default': "'PG'", 'max_length': '2', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'thumb': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'pages.residential_service': {
            'Meta': {'object_name': 'Residential_Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'other_services_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'other_services_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'residential_blurb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'residential_pic': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'service_area_blurb': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
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
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 21, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
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