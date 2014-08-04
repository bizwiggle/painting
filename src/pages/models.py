from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

from auth.models import MyUser

class Home(models.Model):
    description = models.CharField('Home Page Description', max_length=160, 
                                   default='An attention grabbing description goes here (less than 160 characters)') 
    banner_text = models.CharField('First Banner Text', max_length=40,
                                   default='Professional House Painting Service')

class Painting_Site(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)
    home_page = models.ForeignKey(Home)
    phone_number = models.CharField('Business Phone Number', max_length=16, default='Phone Number')  
    # favicon

    def __unicode__(self):
        return unicode(self.site)

