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
       success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        
        'page_title':'Painting Index Title',
        'page_description':'Enter page description',
        'active':'index',
        'general_info':general_info,
        'success_stories':success_stories,
    }
    return render(request, 'index.html', context)

def why_us(request):
    try:
       general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
       services = Services.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Our Process Title',
        'page_description':'Enter page description',
        'active':'why-us',
        'general_info':general_info,
        'services':services,
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
        'page_description':'Enter page description',
        'active':'services',
        'general_info':general_info,
        'services':services,
    }
    return render(request, 'services.html', context)

def residential(request):
    try:
       general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Residential Painting Title',
        'page_description':'Enter page description',
        'active':'services',
        'general_info':general_info,
    }
    return render(request, 'residential.html', context)

def comercial(request):
    try:
       general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Comercial Painting Title',
        'page_description':'Enter page description',
        'active':'services',
        'general_info':general_info,
    }
    return render(request, 'comercial.html', context)

def other(request):
    try:
       general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Other Services Title',
        'page_description':'Enter page description',
        'active':'services',
        'general_info':general_info,
    }
    return render(request, 'other.html', context)

def portfolio(request):
    try:
       general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Portfolio Title',
        'page_description':'Enter page description',
        'active':'portfolio',
        'general_info':general_info,
    }
    return render(request, 'portfolio.html', context)

def about(request):
    try:
       general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
       success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting About Title',
        'page_description':'Enter page description',
        'active':'about',
        'general_info':general_info,
        'success_stories':success_stories,
    }
    return render(request, 'about.html', context)

def contact(request):
    try:
       general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    context = {
        'page_title':'Painting Contact Title',
        'page_description':'Enter page description',
        'active':'contact',
        'general_info':general_info,
    }
    return render(request, 'contact.html', context)

