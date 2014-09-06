#for testing only
from django.http import HttpResponse, Http404

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.contrib import messages

from pages.models import *

def index(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        index = Index.objects.get(site__id__exact=get_current_site(request).id)
        success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        
        'page_title':'Painting Index Title',
#        'page_description':index.meta_description,
        'active':'index',
        'general_info':general_info,
        'index':index,
        'success_stories':success_stories,
    }
    return render(request, 'index.html', context)

def why_us(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
        why_us = Why_Us.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Our Process Title',
 #       'page_description':why_us.meta_description,
        'active':'why-us',
        'general_info':general_info,
        'services':services,
        'why_us':why_us,
    }
    return render(request, 'why_us.html', context)

def services(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting About Title',
  #      'page_description':services.meta_description,
        'active':'services',
        'general_info':general_info,
        'services':services,
        'test':'Q'
    }
    return render(request, 'services.html', context)

def residential(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
        residential_service = Residential_Service.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404
    if not general_info.has_residential_page:
        raise Http404

    context = {
        'page_title':'Painting Residential Painting Title',
   #     'page_description':residential_service.meta_description,
        'active':'services',
        'general_info':general_info,
        'services':services,
        'residential_service':residential_service,
    }
    return render(request, 'residential.html', context)

def comercial(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
        comercial_service = Comercial_Service.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404
    if not general_info.has_comercial_page:
        raise Http404

    context = {
        'page_title':'Painting Comercial Painting Title',
    #    'page_description':comercial_service.meta_description,
        'active':'services',
        'general_info':general_info,
        'services':services,
        'comercial_service':comercial_service,
    }
    return render(request, 'comercial.html', context)

def other(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
        other_services = Other_Services.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404
    if not general_info.has_other_services_page:
        raise Http404

    context = {
        'page_title':'Painting Other Services Title',
     #   'page_description':other_services.meta_description,
        'active':'services',
        'general_info':general_info,
        'services':services,
        'other_services':other_services,
    }
    return render(request, 'other.html', context)

def portfolio(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        portfolio_pics = Portfolio_Pic.objects.filter(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Portfolio Title',
      #  'page_description':general_info.portfolio_meta_description,
        'active':'portfolio',
        'general_info':general_info,
        'portfolio_pics':portfolio_pics,
    }
    return render(request, 'portfolio.html', context)

def about(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
        about  = About.objects.get(site__id__exact=get_current_site(request).id)
        our_people = Our_People.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting About Title',
   #     'page_description':about.meta_description,
        'active':'about',
        'general_info':general_info,
        'success_stories':success_stories,
        'about':about,
        'our_people':our_people,
    }
    return render(request, 'about.html', context)

def contact(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Contact Title',
    #    'page_description':general_info.contact_meta_description,
        'active':'contact',
        'general_info':general_info,
    }
    return render(request, 'contact.html', context)

