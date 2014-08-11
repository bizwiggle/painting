from django.contrib import admin
from pages.models import *

class General_Info_Admin(admin.ModelAdmin):
    pass

admin.site.register(General_Info, General_Info_Admin)

class Success_Stories_Admin(admin.ModelAdmin):
    pass

admin.site.register(Success_Stories, Success_Stories_Admin)

class Services_Admin(admin.ModelAdmin):
    pass

admin.site.register(Services, Services_Admin)
