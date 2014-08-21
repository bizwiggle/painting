#for testing only
from django.http import HttpResponse, Http404

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.contrib import messages

from pages.models import Why_Us 

def dashboard(request):
    context = { 
        'page_title':'Sitename Dashboard',
        'page_description':'Enter page descrption here',
    }  
    return render(request, 'interface/dashboard.html', context)

def general_info(request):
    return HttpResponse('This is the general info page')

def index(request):
    return HttpResonse('This is the index interface')

@login_required
def why_us(request):
    user = request.user
    if not user.is_active:
        # add message
	     # return redirect
	     pass

    # Retrieve Data
    try:
        why_us = Why_Us.objects.get(site__id__exact=get_current_site(request).id)
    except:
        # add new and checkoff the why us on tasks
        raise Http404

    # Check User belongs to this site
    if why_us.user != user:
        # add message
        # return redirect to login
        raise Http404

    use_help_message = True 
    # Process Form
    if request.POST:
        try:
            why_us.reason1 = request.POST.get('reason1', '')
            why_us.reason1_blurb = request.POST.get('reason1_blurb', '')
            if request.POST.get('delete_reason1_pic'):
                why_us.reason1_pic.delete(save=False)
            why_us.save()

            use_help_message = False
        except:
            #add message
            #redirect
            pass

    context = { 
         'page_title':'Sitename Dashboard',
         'page_description':'Enter page descrption here',
         'active_page':'why_us',
         'use_help_message':use_help_message,
         'help_message':'This is the Why Us Help Message',
         'why_us':why_us,
          
    }  
    return render(request, 'interface/why_us.html', context)

