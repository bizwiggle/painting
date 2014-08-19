from django.contrib import admin
from pages.models import *

class General_Info_Admin(admin.ModelAdmin):
    pass

admin.site.register(General_Info, General_Info_Admin)

class Index_Admin(admin.ModelAdmin):
    pass

admin.site.register(Index, Index_Admin)

class Success_Stories_Admin(admin.ModelAdmin):
    pass

admin.site.register(Success_Stories, Success_Stories_Admin)

class Services_Admin(admin.ModelAdmin):
    pass

admin.site.register(Services, Services_Admin)

class Residential_Service_Admin(admin.ModelAdmin):
    pass

admin.site.register(Residential_Service, Residential_Service_Admin)

class Comercial_Service_Admin(admin.ModelAdmin):
    pass

admin.site.register(Comercial_Service, Comercial_Service_Admin)

class Other_Services_Admin(admin.ModelAdmin):
    pass

admin.site.register(Other_Services, Other_Services_Admin)

class Why_Us_Admin(admin.ModelAdmin):
    pass

admin.site.register(Why_Us, Why_Us_Admin)

class Portfolio_Pic_Admin(admin.ModelAdmin):
    pass

admin.site.register(Portfolio_Pic, Portfolio_Pic_Admin)

class About_Admin(admin.ModelAdmin):
    pass

admin.site.register(About, About_Admin)

class Our_People_Admin(admin.ModelAdmin):
    pass

admin.site.register(Our_People, Our_People_Admin)

