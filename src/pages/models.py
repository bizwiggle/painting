# testing and design only
import datetime

from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

from auth.models import MyUser

from painting.constants import STATES 

class General_Info(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)
    
    business_name = models.CharField('Business Name', max_length=64, default='Business Name', blank=True)

    logo = models.ImageField('Business Logo', upload_to=settings.SITE_NAME, null=True, blank=True)   
    logo_small = models.ImageField('Business Logo - small', upload_to=settings.SITE_NAME, null=True, blank=True)

    email = models.EmailField('Email', db_index=True, blank=True)
 
    street_address = models.CharField('Street Address', max_length=64, blank=True)
    extra_address = models.CharField('Extra Address', max_length=32, blank=True)
    city = models.CharField('City', db_index=True, max_length=64, blank=True)
    state = models.CharField('State', db_index=True, max_length=2, choices=STATES, blank=True)
    zip_code = models.CharField('Zip', db_index=True, max_length=5, blank=True)

    phone = models.CharField('Phone Number', max_length=17, blank=True)
    
    fax = models.CharField('Fax Number', max_length=17, blank=True) 

    why_us_brief = models.CharField('Why Choose Us, Brief', max_length=200, blank=True)
    banner_text = models.CharField('Banner Text', max_length=120 , blank=True)

    facebook_URL = models.URLField('Facebook URL', blank=True)
    linkedin_URL = models.URLField('Linkedin URL', blank=True)
    google_plus_URL = models.URLField('Google Plus URL', blank=True)
    twitter_URL = models.URLField('Twitter URL', blank=True)
    tumblr_URL = models.URLField('Tumblr URL', blank=True)
    pintrest_URL = models.URLField('Pintrest URL', blank=True)

    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'General Info'])


class Success_Stories(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)

    story1 = models.CharField('Success Story 1', max_length=256, blank=True)
    story1_name = models.CharField('Success Story 1 Name', max_length=64, blank=True)
    story1_URL = models.URLField('Success Story 1 Link', blank=True)

    story2 = models.CharField('Success Story 2', max_length=256, blank=True)
    story2_name = models.CharField('Success Story 2 Name', max_length=64, blank=True)
    story2_URL = models.URLField('Success Story 2 Link', blank=True)

    story3 = models.CharField('Success Story 3', max_length=256, blank=True)
    story3_name = models.CharField('Success Story 3 Name', max_length=64, blank=True)
    story3_URL = models.URLField('Success Story 3 Link', blank=True)

    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Success Stories'])

class Services(models.Model):
    RESIDENTIAL = 'R'
    COMERCIAL = 'C'
    OTHER = 'O'
    NONE = 'N'
    SERVICE_PAGE_CHOICES = (
        (RESIDENTIAL, 'Residential'),
        (COMERCIAL, 'Comercial'),
        (OTHER, 'Other Services'),
        (NONE, 'No Link'),
    )


    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)

    residential_blurb = models.CharField('Residential Blurb', max_length=256, blank=True)
    residential_pic = models.ImageField('Residential Pic', upload_to=settings.SITE_NAME, null=True, blank=True)

    comercial_blurb = models.CharField('Comercial Blurb', max_length=256, blank=True)
    comercial_pic = models.ImageField('Residential Pic', upload_to=settings.SITE_NAME, null=True, blank=True)
   
    other_services_blurb = models.CharField('Other Services Blurb', max_length=256, blank=True)
    other_services_pic = models.ImageField('Other Services Pic', upload_to=settings.SITE_NAME, null=True, blank=True)

    service_area_blurb = models.CharField('Service Area Blurb', max_length=64, blank=True)

    service_list1 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list1_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list2 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list2_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list3 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list3_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list4 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list4_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list5 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list5_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list6 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list6_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list7 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list7_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list8 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list8_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list9 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list9_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list10 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list10_link = models.CharField('Service List 1', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Services'])


