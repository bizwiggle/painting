from django.conf.urls import patterns, url 

from interface import views

urlpatterns = patterns('',
    url(r'^$', views.interface_dashboard, name='admin_dashboard'),
    url(r'^general_info/$', views.interface_general_info, name='admin_general_info'),
    url(r'^index/$', views.interface_index, name='admin_index'),
    url(r'^why-us/$', views.interface_why_us, name='admin_why_us'),
    url(r'^testimonials/$', views.interface_success_stories, name='admin_success_stories'),
    url(r'^login/$', views.interface_login, name='admin_login'),
)
