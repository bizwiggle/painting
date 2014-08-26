#for testing only
from django.http import HttpResponse, Http404

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.contrib import messages

from pages.models import Why_Us, Success_Stories 
from interface.user_messages import *

@login_required
def interface_dashboard(request):
    context = { 
        'page_title':'Sitename Dashboard',
        'page_description':'Enter page descrption here',
    }  
    return render(request, 'interface/dashboard.html', context)

@login_required
def interface_general_info(request):
    return HttpResponse('This is the general info page')

@login_required
def interface_index(request):
    return HttpResonse('This is the index interface')

@login_required
def interface_why_us(request):
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

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
         'active_page':'admin_why_us',
         'use_help_message':use_help_message,
         'help_message':'This is the Why Us Help Message',
         'why_us':why_us,
    }  
    return render(request, 'interface/why_us.html', context)

@login_required
def interface_success_stories(request):
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # return redirect
        return redirect('admin_login')

    # Retrieve Data
    try:
        success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
    except:
        # checkoff the why us on tasks
        raise Http404
    
    # Check User belongs to this site
    if success_stories.user != user:
        # add message
        # return redirect to login
        raise Http404

    use_help_message = True 
    if request.POST:
        try:
            success_stories.story1 = request.POST.get('story1', '')
            success_stories.story1_name = request.POST.get('story1_name', '')
            success_stories.story1_URL = request.POST.get('story1_URL', '')
            success_stories.save()
            use_help_message = False
            messages.success(request, "Your 'Testimonials' have been successfully been updated.")
        except:
            messages.warning(request, "A problem happened and it's not your fault!  A technical dificulty caused us to not be able to save your 'Testimonials'.  Please try again or contact Bizwiggle for help.")
   

    context = { 
         'page_title':'Testimonial Admin',
         'page_description':'Enter page descrption here',
         'active_page':'admin_success_stories',
         'use_help_message':use_help_message,
         'help_message':'This is the Testimonial Page Help Message',
         'success_stories':success_stories,
    }  
    return render(request, 'interface/success_stories.html', context)
   

def interface_login(request):
    return HttpResponse('This is the login for admin page')
 
