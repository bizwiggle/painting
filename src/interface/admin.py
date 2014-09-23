from django.contrib import admin

from interface.models import *

class Progress_Admin(admin.ModelAdmin):
    pass

admin.site.register(Progress, Progress_Admin)

class Billing_Admin(admin.ModelAdmin):
    pass

admin.site.register(Billing, Billing_Admin)

