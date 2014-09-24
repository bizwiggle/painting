from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

from auth.models import MyUser

class Progress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)

    has_general = models.BooleanField('Has General Info Filled Out', default=False)
    has_index = models.BooleanField('Has Home Info Filled Out', default=False)
    has_why_us = models.BooleanField('Has Why Us Filled Out', default=False)
    has_about = models.BooleanField('Has About Filled Out', default=False)
    has_success_stories = models.BooleanField('Has Success Stories Filled Out', default=False)
    has_services = models.BooleanField('Has Services Filled Out', default=False)
    has_residential_services =  models.BooleanField('Has Residential Services Filled Out', default=False)
    has_comercial_services =  models.BooleanField('Has Commercial Services Filled Out', default=False)
    has_portfolio =  models.BooleanField('Has Image added to portfolio', default=False)
    has_other_services =  models.BooleanField('Has Other Services Filled Out', default=False)
    has_social =  models.BooleanField('Has Social Information Filled Out', default=False)
    has_our_people =  models.BooleanField('Has Our People Filled Out', default=False)
    has_seo_tools =  models.BooleanField('Has SEO Tools Filled Out', default=False)
    has_billing = models.BooleanField('Has SEO Tools Filled Out', default=False)

    business_name = models.CharField('Business Name', max_length=64, default="Business Name Here", blank=True)

    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Progress'])

class Billing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    stripe_id = models.CharField('Stripe ID of a user', max_length=120, null=True, blank=True)
    stripe_id_website_sub = models.CharField('Stripe ID of website subscription', max_length=120, null=True, blank=True)

    def __unicode__(self):
        return ' - '.join(['Billing', self.user.email, self.stripe_id])
