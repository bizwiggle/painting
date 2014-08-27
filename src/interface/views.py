#for testing only
from django.http import HttpResponse, Http404

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.contrib import messages

from pages.models import (Why_Us, Success_Stories, About, Services) 

from interface.models import Progress 
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
    return HttpResponse('This is the index interface')

@login_required
def interface_about(request):
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    # Retrieve Data
    try:
        about = About.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    # Check User belongs to this site
    if about.user != user or progress.user != user:
        # add message
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            about.headline = request.POST.get('headline', '')
            about.text = request.POST.get('text', '')
            if request.POST.get('delete_pic'):
                about.pic.delete(save=False)
            if request.FILES.get('pic'):
                about.pic = request.FILES.get('pic')

            about.info_headline = request.POST.get('info_headline', '')
            about.info1 = request.POST.get('info1', '')
            about.info2 = request.POST.get('info2', '')
            about.info3 = request.POST.get('info3', '')
            about.info4 = request.POST.get('info4', '')
            about.info5 = request.POST.get('info5', '')
           
            about.save()
            
            progress.has_about = True
            progress.save()

            use_help_message = False
            messages.success(request, "Your 'About' has successfully been updated.")
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title':'Sitename Dashboard',
         'page_description':'Enter page descrption here',
         'active_page':'admin_about',
         'use_help_message':use_help_message,
         'help_message':'This is the About Help Message',
         'about':about,
         'progress':progress,
    }  
    return render(request, 'interface/about.html', context)

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
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    # Check User belongs to this site
    if why_us.user != user or progress.user != user:
        # add message
        return redirect('admin_login')

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
            
            progress.has_why_us = True
            progress.save()

            use_help_message = False
            messages.success(request, "Your 'Why Us' has successfully been updated.")
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title':'Sitename Dashboard',
         'page_description':'Enter page descrption here',
         'active_page':'admin_why_us',
         'use_help_message':use_help_message,
         'help_message':'This is the Why Us Help Message',
         'why_us':why_us,
         'progress':progress,
    }  
    return render(request, 'interface/why_us.html', context)

@login_required
def interface_services(request):
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    # Retrieve Data
    try:
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    # Check User belongs to this site
    if services.user != user or progress.user != user:
        # add message
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            services.residential_blurb = request.POST.get('residential_blurb', '')
            if request.POST.get('delete_residential_pic'):
                services.residential_pic.delete(save=False)
            if request.FILES.get('residential_pic'):
                services.residential_pic = request.FILES.get('residential_pic')
            
            services.comercial_blurb = request.POST.get('comercial_blurb', '')
            if request.POST.get('delete_comercial_pic'):
                services.comercial_pic.delete(save=False)
            if request.FILES.get('comercial_pic'):
                services.comercial_pic = request.FILES.get('comercial_pic')

            services.other_services_blurb = request.POST.get('other_services_blurb', '')
            if request.POST.get('delete_other_services_pic'):
                services.other_services_pic.delete(save=False)
            if request.FILES.get('other_services_pic'):
                services.other_services_pic = request.FILES.get('other_services_pic')

            services.service_list1 = request.POST.get('service_list1', '')
            services.service_list1_link = request.POST.get('service_list1_link', '')
            services.service_list2 = request.POST.get('service_list2', '')
            services.service_list2_link = request.POST.get('service_list2_link', '')
            services.service_list3 = request.POST.get('service_list3', '')
            services.service_list3_link = request.POST.get('service_list3_link', '')
            services.service_list4 = request.POST.get('service_list4', '')
            services.service_list4_link = request.POST.get('service_list4_link', '')
            services.service_list5 = request.POST.get('service_list5', '')
            services.service_list5_link = request.POST.get('service_list5_link', '')
            services.service_list6 = request.POST.get('service_list6', '')
            services.service_list6_link = request.POST.get('service_list6_link', '')
            services.service_list7 = request.POST.get('service_list7', '')
            services.service_list7_link = request.POST.get('service_list7_link', '')
            services.service_list8 = request.POST.get('service_list8', '')
            services.service_list8_link = request.POST.get('service_list8_link', '')
            services.service_list9 = request.POST.get('service_list9', '')
            services.service_list9_link = request.POST.get('service_list9_link', '')
            services.service_list10 = request.POST.get('service_list10', '')
            services.service_list10_link = request.POST.get('service_list10_link', '')

            services.service_area_blurb = request.POST.get('service_area_blurb', '')            
            services.save()

            progress.has_services = True
            progress.save()

            use_help_message = False
            messages.success(request, "Your 'Services' have successfully been updated.")
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title':'Site Admin Services',
         'page_description':'Enter page descrption here',
         'active_page':'admin_services',
         'use_help_message':use_help_message,
         'help_message':SERVICES_HELP_MESSAGE,
         'services':services,
         'progress':progress,
    }  
    return render(request, 'interface/services.html', context)

@login_required
def interface_residential(request):
    return HttpResponse('This is the admin residential page')

@login_required
def interface_comercial(request):
    return HttpResponse('This is the admin commercial page')

@login_required
def interface_other_services(request):
    return HttpResponse('This is the admin other services page')

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
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404
    
    # Check User belongs to this site
    if success_stories.user != user or progress.user != user:
        # add message
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            success_stories.story1 = request.POST.get('story1', '')
            success_stories.story1_name = request.POST.get('story1_name', '')
            success_stories.story1_URL = request.POST.get('story1_URL', '')
            success_stories.story2 = request.POST.get('story2', '')
            success_stories.story2_name = request.POST.get('story2_name', '')
            success_stories.story2_URL = request.POST.get('story2_URL', '')
            success_stories.story3 = request.POST.get('story3', '')
            success_stories.story3_name = request.POST.get('story3_name', '')
            success_stories.story3_URL = request.POST.get('story3_URL', '')
            success_stories.other_URL = request.POST.get('other_URL', '')      

            success_stories.save()

            progress.has_success_stories = True
            progress.save()
            
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
         'progress':progress,
    }  
    return render(request, 'interface/success_stories.html', context)
   

def interface_login(request):
    return HttpResponse('This is the login for admin page')
 
