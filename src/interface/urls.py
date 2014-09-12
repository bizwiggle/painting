from django.conf.urls import patterns, url 

from interface import views

urlpatterns = patterns('',
    url(r'^$', views.interface_dashboard, name='admin_dashboard'),
    url(r'^general_info/$', views.interface_general_info, name='admin_general_info'),
    url(r'^home/$', views.interface_index, name='admin_index'),
    url(r'^about/$', views.interface_about, name='admin_about'),
    url(r'^services/$', views.interface_services, name='admin_services'),
    url(r'^residential/$', views.interface_residential, name='admin_residential'),
    url(r'^commercial/$', views.interface_comercial, name='admin_comercial'),
    url(r'^other-services/$', views.interface_other_services, name='admin_other_services'),
    url(r'^add-portfolio/$', views.interface_add_portfolio, name='admin_add_portfolio'),
    url(r'^edit-portfolio/$', views.interface_edit_portfolio, name='admin_edit_portfolio'),
    url(r'^why-us/$', views.interface_why_us, name='admin_why_us'),
    url(r'^our-people/$', views.interface_our_people, name='admin_our_people'),
    url(r'^social/$', views.interface_social, name='admin_social'),
    url(r'^testimonials/$', views.interface_success_stories, name='admin_success_stories'),
    url(r'^seo_tools/$', views.interface_seo_tools, name='admin_seo_tools'),
    url(r'^login/$', views.interface_login, name='admin_login'),
    url(r'^forgot-password/$', views.interface_forgot_password, name='admin_forgot_password'),
    url(r'^logout/$', views.interface_logout, name='admin_logout'),
)

