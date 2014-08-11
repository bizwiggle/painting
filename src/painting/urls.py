from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^why_us/$', views.why_us, name='why-us'),
    url(r'^services/$', views.services, name='services'),
    url(r'^services/residential/$', views.residential, name='residential'),
    url(r'^services/comercial/$', views.comercial, name='comercial'),
    url(r'^services/other/$', views.other, name='other'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^wiggle/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
