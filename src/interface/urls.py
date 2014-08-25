from django.conf.urls import patterns, url 

from interface import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='admin_dashboard'),
    url(r'^general_info/$', views.general_info, name='admin_general_info'),
    url(r'^index/$', views.index, name='admin_index'),
    url(r'^why-us/$', views.why_us_admin, name='admin_why_us'),
)

