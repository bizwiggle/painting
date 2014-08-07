from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

from auth.models import MyUser

class General_Info(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)
    
    business_name = models.CharField('Business Name', max_length=64, default='Business Name')
    
    street_address = 
    extra_address = 
    city = 
    state = 
    zip_code = 

    phone =
    fax = 
  
    logo
    logo_sm


class Social(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)


