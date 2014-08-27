from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

from auth.models import MyUser

class Progress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)

    has_why_us = models.BooleanField('Has Why Us Filled Out', default=False)
    has_about = models.BooleanField('Has About Filled Out', default=False)
    has_success_stories = models.BooleanField('Has Success Stories Filled Out', default=False)
    has_services = models.BooleanField('Has Services Filled Out', default=False)

    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Progress'])
