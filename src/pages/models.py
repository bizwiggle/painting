# testing and design only
import datetime

from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

from imagekit.models import ProcessedImageField, ImageSpecField 
from imagekit.processors import ResizeToFit, ResizeToFill, SmartResize

from auth.models import MyUser

from painting.constants import STATES 

class General_Info(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)
    
    business_name = models.CharField('Business Name', max_length=64, default='Business Name', blank=True)

    has_residential_page = models.BooleanField('Has Residential Page', default=True)
    has_comercial_page = models.BooleanField('Has Commercial Page', default=True)
    has_other_services_page = models.BooleanField('Has Other Services Page', default=True)

    logo  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                processors=[ResizeToFit(400, 62)],
                                options={'quality': 100},
			                       null=True,
                                blank=True,
            )

    logo_small  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                      processors=[ResizeToFit(200, 31)],
                                      options={'quality': 100},
			                             null=True,
                                      blank=True,
                  )

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

    contact_meta_description = models.CharField('Contact Meta Descrption', max_length=160, blank=True)
    portfolio_meta_description = models.CharField('Portfolio Meta Descrption', max_length=160, blank=True)
 
    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'General Info'])


class Index(models.Model):
    WHY_US = 'Why Us'
    SERVICES = 'Services'
    RESIDENTIAL = 'Residential Painting'
    COMERCIAL = 'Comercial Painting'
    OTHER = 'Other Services'
    PORTFOLIO = 'Portfolio'
    ABOUT = 'About Us'
    CONTACT  = 'Contact'
    PAGES_CHOICES = (
        (WHY_US,'Why Us'),
        (SERVICES,'Services'),
        (RESIDENTIAL,'Residential Painting'),
        (COMERCIAL,'Comercial Painting'),
        (OTHER,'Other Services'),
        (PORTFOLIO,'Portfolio'),
        (ABOUT,'About Us'),
        (CONTACT,'Contact'),
    )
    DEFAULT_SLIDER_TXT_TOP='Request a'
    DEFAULT_SLIDER_TXT_BOTTOM='Hassle Free Estimate'

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)
    
    slider_txt_top1 = models.CharField('Banner Text Top 1', max_length=32, blank=True,default=DEFAULT_SLIDER_TXT_TOP,)
    slider_txt_bottom1 = models.CharField('Slider Text Bottom 1', max_length=32, blank=True, default=DEFAULT_SLIDER_TXT_BOTTOM)
    slider_link1 = models.CharField('Slider Link 1', max_length=30, blank=True, choices=PAGES_CHOICES, default=CONTACT) 

    slider_txt_top2 = models.CharField('Banner Text Top 2', max_length=32, blank=True,default=DEFAULT_SLIDER_TXT_TOP,)
    slider_txt_bottom2 = models.CharField('Slider Text Bottom 2', max_length=32, blank=True, default=DEFAULT_SLIDER_TXT_BOTTOM)
    slider_link2 = models.CharField('Slider Link 2', max_length=30, blank=True, choices=PAGES_CHOICES, default=CONTACT) 

    slider_txt_top3 = models.CharField('Banner Text Top 3', max_length=32, blank=True,default=DEFAULT_SLIDER_TXT_TOP,)
    slider_txt_bottom3 = models.CharField('Slider Text Bottom 3', max_length=32, blank=True, default=DEFAULT_SLIDER_TXT_BOTTOM)
    slider_link3 = models.CharField('Slider Link 3', max_length=30, blank=True, choices=PAGES_CHOICES, default=CONTACT) 

    slider_txt_top4 = models.CharField('Banner Text Top 4', max_length=32, blank=True,default=DEFAULT_SLIDER_TXT_TOP,)
    slider_txt_bottom4 = models.CharField('Slider Text Bottom 4', max_length=32, blank=True, default=DEFAULT_SLIDER_TXT_BOTTOM)
    slider_link4 = models.CharField('Slider Link 4', max_length=30, blank=True, choices=PAGES_CHOICES, default=CONTACT) 

    slider_txt_top5 = models.CharField('Banner Text Top 5', max_length=32, blank=True,default=DEFAULT_SLIDER_TXT_TOP,)
    slider_txt_bottom5 = models.CharField('Slider Text Bottom 5', max_length=32, blank=True, default=DEFAULT_SLIDER_TXT_BOTTOM)
    slider_link5 = models.CharField('Slider Link 5', max_length=30, blank=True, choices=PAGES_CHOICES, default=CONTACT) 

    why_us_blurb = models.CharField('Why Us Home Blurb', max_length=160, blank=True)
    about_blurb = models.CharField('About Us Home Blurb', max_length=160, blank=True)
    
    hello_title = models.CharField('Hello Title', max_length=48, blank=True)
    hello_txt = models.CharField('Hello Txt', max_length=512, blank=True)
    hello_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                     processors=[ResizeToFit(169, 284)],
                                     options={'quality': 80},
			                            null=True,
                                     blank=True,
                 )

    affilation_pic1  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                     processors=[ResizeToFit(120, 50)],
                                     options={'quality': 80},
			                            null=True,
                                     blank=True,
                      )
  
    affilation_pic2  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                     processors=[ResizeToFit(120, 50)],
                                     options={'quality': 80},
			                            null=True,
                                     blank=True,
                      )
  
    affilation_pic3  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                     processors=[ResizeToFit(120, 50)],
                                     options={'quality': 80},
			                            null=True,
                                     blank=True,
                      )
  
    affilation_pic4  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                     processors=[ResizeToFit(120, 50)],
                                     options={'quality': 80},
			                            null=True,
                                     blank=True,
                      )
  
    affilation_pic5  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                     processors=[ResizeToFit(120, 50)],
                                     options={'quality': 80},
			                            null=True,
                                     blank=True,
                      )
 
    affilation_pic6  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                     processors=[ResizeToFit(120, 50)],
                                     options={'quality': 80},
			                            null=True,
                                     blank=True,
                      )
    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Index'])

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

    other_URL = models.URLField('Other URL', blank=True)

    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
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
    residential_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                           processors=[ResizeToFill(214, 214)],
                                           options={'quality': 80},
			                                  null=True,
                                           blank=True,
                       )

    comercial_blurb = models.CharField('Comercial Blurb', max_length=256, blank=True)
    comercial_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                         processors=[ResizeToFill(214, 214)],
                                         options={'quality': 80},
			                                null=True,
                                         blank=True,
                     )
   
    other_services_blurb = models.CharField('Other Services Blurb', max_length=256, blank=True)
    other_services_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                              processors=[ResizeToFill(214, 214)],
                                              options={'quality': 80},
			                                     null=True,
                                              blank=True,
                          )

    service_area_blurb = models.CharField('Service Area Blurb', max_length=64, blank=True)

    service_list1 = models.CharField('Service List 1', max_length=64, blank=True)
    service_list1_link = models.CharField('Service List 1 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list2 = models.CharField('Service List 2', max_length=64, blank=True)
    service_list2_link = models.CharField('Service List 2 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list3 = models.CharField('Service List 3', max_length=64, blank=True)
    service_list3_link = models.CharField('Service List 3 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list4 = models.CharField('Service List 4', max_length=64, blank=True)
    service_list4_link = models.CharField('Service List 4 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list5 = models.CharField('Service List 5', max_length=64, blank=True)
    service_list5_link = models.CharField('Service List 5 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list6 = models.CharField('Service List 6', max_length=64, blank=True)
    service_list6_link = models.CharField('Service List 6 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list7 = models.CharField('Service List 7', max_length=64, blank=True)
    service_list7_link = models.CharField('Service List 7 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list8 = models.CharField('Service List 8', max_length=64, blank=True)
    service_list8_link = models.CharField('Service List 8 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list9 = models.CharField('Service List 9', max_length=64, blank=True)
    service_list9_link = models.CharField('Service List 9 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    service_list10 = models.CharField('Service List 10', max_length=64, blank=True)
    service_list10_link = models.CharField('Service List 10 Link', max_length=1, blank=True, choices=SERVICE_PAGE_CHOICES, default=NONE)

    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Services'])


class Residential_Service(models.Model):
    PAGE_NAME = "Residential Service"
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)

    pic1  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
             )
    
    pic2  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
            )
    
    pic3  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
           )
    
    paragraph_headline1 = models.CharField('Paragraph 1 Headline', max_length=64, blank=True)
    paragraph1 = models.CharField('Paragraph 1', max_length=512, blank=True)

    paragraph_headline2 = models.CharField('Paragraph 2 Headline', max_length=64, blank=True)
    paragraph2 = models.CharField('Paragraph 2', max_length=512, blank=True)
	 
    paragraph_headline3 = models.CharField('Paragraph 3 Headline', max_length=64, blank=True)
    paragraph3 = models.CharField('Paragraph 3', max_length=512, blank=True)

    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Residential Service'])

class Comercial_Service(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)

    pic1  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
             )
    
    pic2  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
            )
    
    pic3  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
           )
    
    paragraph_headline1 = models.CharField('Paragraph 1 Headline', max_length=64, blank=True)
    paragraph1 = models.CharField('Paragraph 1', max_length=512, blank=True)

    paragraph_headline2 = models.CharField('Paragraph 2 Headline', max_length=64, blank=True)
    paragraph2 = models.CharField('Paragraph 2', max_length=512, blank=True)
	 
    paragraph_headline3 = models.CharField('Paragraph 3 Headline', max_length=64, blank=True)
    paragraph3 = models.CharField('Paragraph 3', max_length=512, blank=True)

    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Comercial Service'])

class Other_Services(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)
    
    pic1  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
             )
    
    pic2  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
            )
    
    pic3  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
           )
    
    pic4  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
           )

    pic5  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                          processors=[ResizeToFill(214, 214)],
                                          options={'quality': 80},
                                          null=True,
                                          blank=True,
           )

    service_headline1 = models.CharField('Service 1 Headline', max_length=64, blank=True)
    service1 = models.CharField('Service 1', max_length=512, blank=True)

    service_headline2 = models.CharField('Service 2 Headline', max_length=64, blank=True)
    service2 = models.CharField('Service 2', max_length=512, blank=True)
	 
    service_headline3 = models.CharField('Service 3 Headline', max_length=64, blank=True)
    service3 = models.CharField('Service 3', max_length=512, blank=True)

    service_headline4 = models.CharField('Service 4 Headline', max_length=64, blank=True)
    service4 = models.CharField('Service 4', max_length=512, blank=True)
    
    service_headline5 = models.CharField('Service 5 Headline', max_length=64, blank=True)
    service5 = models.CharField('Service 5', max_length=512, blank=True)
    
    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Other Services'])

class Why_Us(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)
    
    reason1 = models.CharField('Reason 1', max_length=48, blank=True)
    reason1_blurb = models.CharField('Reason 1 Blurb', max_length=350, blank=True)
    reason1_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                       processors=[ResizeToFill(210, 146)],
                                       options={'quality': 80},
			                              null=True,
                                       blank=True,
                   )  
    
    reason2 = models.CharField('Reason 2', max_length=48, blank=True)
    reason2_blurb = models.CharField('Reason 2 Blurb', max_length=350, blank=True)
    reason2_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                       processors=[ResizeToFill(210, 146)],
                                       options={'quality': 80},
			                              null=True,
                                       blank=True,
                   )  

    reason3 = models.CharField('Reason 3', max_length=48, blank=True)
    reason3_blurb = models.CharField('Reason 3 Blurb', max_length=350, blank=True)
    reason3_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                       processors=[ResizeToFill(210, 146)],
                                       options={'quality': 80},
			                              null=True,
                                       blank=True,
                   )  

    reason4 = models.CharField('Reason 4', max_length=48, blank=True)
    reason4_blurb = models.CharField('Reason 4 Blurb', max_length=350, blank=True)
    reason4_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                       processors=[ResizeToFill(210, 146)],
                                       options={'quality': 80},
			                              null=True,
                                       blank=True,
                   )  

    reason5 = models.CharField('Reason 5', max_length=48, blank=True)
    reason5_blurb = models.CharField('Reason 5 Blurb', max_length=350, blank=True)
    reason5_pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                       processors=[ResizeToFill(210, 146)],
                                       options={'quality': 80},
			                              null=True,
                                       blank=True,
                   )  
    
    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Why_Us'])

class Portfolio_Pic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)

    INTERRIOR_PIC = 'I'
    EXTERRIOR_PIC = 'E'
    COMERCIAL_PIC = 'C'
    OTHER_PIC = 'O'
    WORK_PIC = 'W' 	 

    PIC_TYPE_CHOICES = (
        (INTERRIOR_PIC, 'Interrior Pic'),
        (EXTERRIOR_PIC, 'Exterrior Pic'),
        (COMERCIAL_PIC, 'Comercial Pic'),
        (OTHER_PIC, 'Other Pic'),
        (WORK_PIC, 'Work Pic'),
    )
    thumb = ProcessedImageField(upload_to=settings.SITE_NAME,
                                processors=[ResizeToFill(290, 193)],
                                options={'quality': 100},
			                       null=True,
                                blank=True,
            )

    pic = ProcessedImageField(upload_to=settings.SITE_NAME,
                              processors=[ResizeToFit(870, 291)],
                              options={'quality': 100},
			                     null=True,
                              blank=True,
          )
    pic_type = models.CharField('Pic Type', max_length=1, blank=True, choices=PIC_TYPE_CHOICES)
    
    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'Portfolio Pic'])

class About(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)

    headline = models.CharField('About Headline', max_length=64, blank=True)
    text = models.CharField('About Text', max_length=512, blank=True)

    pic = ProcessedImageField(upload_to=settings.SITE_NAME,
                              processors=[ResizeToFill(350, 350)],
                              options={'quality': 100},
			                     null=True,
                              blank=True,
          )
    
    info_headline = models.CharField('Info Headline', max_length=32, blank=True, default='The Bottom Line')
    info1 = models.CharField('Info Item 1', max_length=64, blank=True)
    info2 = models.CharField('Info Item 2', max_length=64, blank=True)
    info3 = models.CharField('Info Item 3', max_length=64, blank=True)
    info4 = models.CharField('Info Item 4', max_length=64, blank=True)
    info5 = models.CharField('Info Item 5', max_length=64, blank=True)

    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'About'])

class Our_People(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    site = models.ForeignKey(Site)
   
    headline = models.CharField('Headline', max_length=48, blank=True)
    text = models.CharField('Text', max_length=256, blank=True)

    pic  = ProcessedImageField(upload_to=settings.SITE_NAME,
                                         processors=[ResizeToFill(214, 214)],
                                         options={'quality': 80},
                                         null=True,
                                         blank=True,
           )
    
    last_modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return ' - '.join([unicode(self.site), 'About', self.headline])
