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
def why_us_admin(request):
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
    if request.POST:
        try:
            why_us.reason1 = request.POST.get('reason1', '')
            why_us.reason1_blurb = request.POST.get('reason1_blurb', '')
            if request.POST.get('delete_reason1_pic'):
                why_us.reason1_pic.delete(save=False)
            if request.FILES.get('reason1_pic'):
                why_us.reason1_pic = request.FILES.get('reason1_pic')
          
            why_us.reason2 = request.POST.get('reason2', '')
            why_us.reason2_blurb = request.POST.get('reason2_blurb', '')
            if request.POST.get('delete_reason2_pic'):
                why_us.reason2_pic.delete(save=False)
            if request.FILES.get('reason2_pic'):
                why_us.reason2_pic = request.FILES.get('reason2_pic')
          
            why_us.reason3 = request.POST.get('reason3', '')
            why_us.reason3_blurb = request.POST.get('reason3_blurb', '')
            if request.POST.get('delete_reason3_pic'):
                why_us.reason3_pic.delete(save=False)
            if request.FILES.get('reason3_pic'):
                why_us.reason1_pic = request.FILES.get('reason3_pic')

            why_us.reason4 = request.POST.get('reason4', '')
            why_us.reason4_blurb = request.POST.get('reason4_blurb', '')
            if request.POST.get('delete_reason4_pic'):
                why_us.reason1_pic.delete(save=False)
            if request.FILES.get('reason4_pic'):
                why_us.reason4_pic = request.FILES.get('reason4_pic')
            
            why_us.reason5 = request.POST.get('reason5', '')
            why_us.reason5_blurb = request.POST.get('reason5_blurb', '')
            if request.POST.get('delete_reason5_pic'):
                why_us.reason5_pic.delete(save=False)
            if request.FILES.get('reason5_pic'):
                why_us.reason1_pic = request.FILES.get('reason5_pic')
        
            why_us.save()
            use_help_message = False
            messages.success(request, "Your 'Why Us' has successfully been updated.")
        except:
            messages.warning(request, "A problem happened and it's not your fault!  A technical dificulty caused us to not be able to save your 'Why Us'.  Please try again or contact Bizwiggle for help.")
   
    context = { 
         'page_title':'Sitename Dashboard',
         'page_description':'Enter page descrption here',
         'active_page':'why_us',
         'use_help_message':use_help_message,
         'help_message':'This is the Why Us Help Message',
         'why_us':why_us,
    }  
    return render(request, 'interface/why_us.html', context)

