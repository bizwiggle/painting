import re
import uuid
import datetime
from string import Template

import stripe

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.sites.models import get_current_site
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.sites.models import Site

from painting.stripe_info import PUB_KEY, SECRET_KEY
from painting.constants import STATES, BIZWIGGLE_INFO

from auth.models import MyUser

from pages.models import (Why_Us, Success_Stories, About, Services, Residential_Service,
    Comercial_Service, Other_Services, General_Info, Our_People, Index, Portfolio_Pic
) 

from interface.models import Progress, Billing
from interface.user_messages import *
from interface.billing_functions import (get_customer, update_stripe_email, get_current_subscription,
    get_default_card, is_subscription_canceled, is_subscription_on, is_subscription_unpaid,
    end_subscription_datetime, create_new_subscription, turn_off_subscription, 
)

@login_required
def interface_dashboard(request):
    PAGE_NAME = "Dashboard"
    user = request.user

    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    first_login = False
    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        first_login = True
    
    if first_login:
        create_user_objects(request)
        try:
            progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        except:
            raise Http404    

    if not user.is_superuser and not first_login and progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    return redirect('admin_general_info') 

@login_required
def interface_general_info(request):
    PAGE_NAME = "General Info"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (progress.user != user or general_info.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            general_info.business_name = request.POST.get('business_name', '')
            general_info.email = request.POST.get('email', '')
            general_info.phone = request.POST.get('phone', '')
            general_info.fax = request.POST.get('fax', '')
            general_info.street_address = request.POST.get('street_address', '')
            general_info.extra_address = request.POST.get('extra_address', '')
            general_info.city = request.POST.get('city', '')
            general_info.state = request.POST.get('state', '')
            general_info.zip_code = request.POST.get('zip_code', '')
           
            if request.POST.get('logo') or request.POST.get('delete_logo'):
                general_info.logo.delete(save=False)
                general_info.logo_small.delete(save=False)
            if request.FILES.get('logo'):
                general_info.logo = request.FILES.get('logo')
                general_info.logo_small = request.FILES.get('logo')
            
            general_info.why_us_brief = request.POST.get('why_us_brief', '')
            general_info.banner_text = request.POST.get('banner_text', '')
            
            general_info.save()
        
            progress.business_name = request.POST.get('business_name', '')    
            progress.has_general = True
            progress.save()

            use_help_message = False
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_general',
         'use_help_message':use_help_message,
         'help_message':GENERAL_INFO_HELP_MESSAGE,
         'STATES':STATES,
         'general_info':general_info,
         'progress':progress,
    }  
    return render(request, 'interface/general.html', context)


@login_required
def interface_index(request):
    PAGE_NAME = "Home"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        index = Index.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (index.user != user or progress.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            index.slider_pic = request.POST.get('slider_pic', '')

            index.slider_txt_top1 = request.POST.get('slider_txt_top1', '')
            index.slider_txt_bottom1 = request.POST.get('slider_txt_bottom1', '')
            index.slider_link1 = request.POST.get('slider_link1', '')
           
            index.slider_txt_top2 = request.POST.get('slider_txt_top2', '')
            index.slider_txt_bottom2 = request.POST.get('slider_txt_bottom2', '')
            index.slider_link2 = request.POST.get('slider_link2', '')
            
            index.slider_txt_top3 = request.POST.get('slider_txt_top3', '')
            index.slider_txt_bottom3 = request.POST.get('slider_txt_bottom3', '')
            index.slider_link3 = request.POST.get('slider_link3', '')
           
            index.slider_txt_top4 = request.POST.get('slider_txt_top4', '')
            index.slider_txt_bottom4 = request.POST.get('slider_txt_bottom4', '')
            index.slider_link4 = request.POST.get('slider_link4', '')

            index.slider_txt_top5 = request.POST.get('slider_txt_top5', '')
            index.slider_txt_bottom5 = request.POST.get('slider_txt_bottom5', '')
            index.slider_link5 = request.POST.get('slider_link5', '')

            index.why_us_blurb = request.POST.get('why_us_blurb', '')
            index.about_blurb = request.POST.get('about_blurb', '')

            index.hello_title = request.POST.get('hello_title', '')
            index.hello_txt = request.POST.get('hello_txt', '')

            if request.POST.get('delete_hello_pic'):
                index.hello_pic.delete(save=False)
            if request.FILES.get('hello_pic'):
                index.hello_pic = request.FILES.get('hello_pic')
            
            if request.POST.get('delete_affilation_pic1'):
                index.affilation_pic1.delete(save=False)
            if request.FILES.get('affilation_pic1'):
                index.affilation_pic1 = request.FILES.get('affilation_pic1')
            index.affilation1_URL = request.POST.get('affilation1_URL', '')
 
            if request.POST.get('delete_affilation_pic2'):
                index.affilation_pic2.delete(save=False)
            if request.FILES.get('affilation_pic2'):
                index.affilation_pic2 = request.FILES.get('affilation_pic2')
            index.affilation2_URL = request.POST.get('affilation2_URL', '')
 
            if request.POST.get('delete_affilation_pic3'):
                index.affilation_pic3.delete(save=False)
            if request.FILES.get('affilation_pic3'):
                index.affilation_pic3 = request.FILES.get('affilation_pic3')
            index.affilation3_URL = request.POST.get('affilation3_URL', '')
 
            if request.POST.get('delete_affilation_pic4'):
                index.affilation_pic4.delete(save=False)
            if request.FILES.get('affilation_pic4'):
                index.affilation_pic4 = request.FILES.get('affilation_pic4')
            index.affilation4_URL = request.POST.get('affilation4_URL', '')
 
            if request.POST.get('delete_affilation_pic5'):
                index.affilation_pic5.delete(save=False)
            if request.FILES.get('affilation_pic5'):
                index.affilation_pic5 = request.FILES.get('affilation_pic5')
            index.affilation5_URL = request.POST.get('affilation5_URL', '')
 
            if request.POST.get('delete_affilation_pic6'):
                index.affilation_pic6.delete(save=False)
            if request.FILES.get('affilation_pic6'):
                index.affilation_pic6 = request.FILES.get('affilation_pic6')
            index.affilation6_URL = request.POST.get('affilation6_URL', '')
          
            index.save()
            
            progress.has_index = True
            progress.save()

            use_help_message = False
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_index',
         'use_help_message':use_help_message,
         'help_message':INDEX_HELP_MESSAGE,
         'index':index,
         'progress':progress,
    }  
    return render(request, 'interface/index.html', context)

@login_required
def interface_about(request):
    PAGE_NAME = "About" 
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        about = About.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (about.user != user or progress.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
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
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_about',
         'use_help_message':use_help_message,
         'help_message':'This is the About Help Message',
         'about':about,
         'progress':progress,
    }  
    return render(request, 'interface/about.html', context)

@login_required
def interface_social(request):
    PAGE_NAME = "Social Links" 

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (general_info.user != user or progress.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            general_info.facebook_URL = request.POST.get('facebook_url', '')
            general_info.linkedin_URL = request.POST.get('linkedin_url', '')
            general_info.google_plus_URL = request.POST.get('google_plus_url', '')
            general_info.twitter_URL = request.POST.get('twitter_url', '')
            general_info.tumblr_URL = request.POST.get('tumblr_url', '')
            general_info.pintrest_URL = request.POST.get('pinterest_url', '')
            general_info.save()
            
            progress.has_social = True
            progress.save()

            use_help_message = False
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_social',
         'use_help_message':use_help_message,
         'help_message':SOCIAL_HELP_MESSAGE,
         'general_info':general_info,
         'progress':progress,
    }  
    return render(request, 'interface/social.html', context)

@login_required
def interface_why_us(request):
    PAGE_NAME="Why Us"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        why_us = Why_Us.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (why_us.user != user or progress.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
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
                why_us.reason3_pic = request.FILES.get('reason3_pic')

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
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
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
    PAGE_NAME = "Services Overview"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (services.user != user or progress.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
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
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
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
    PAGE_NAME = "Residential Service" 

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        residential_service = Residential_Service.objects.get(site__id__exact=get_current_site(request).id)
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (residential_service.user != user or progress.user != user or general_info.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            if request.POST.get('has_residential') == 'on':
                general_info.has_residential_page = True 
            else:
                general_info.has_residential_page = False 

            residential_service.paragraph_headline1 = request.POST.get('paragraph_headline1', '')
            residential_service.paragraph1 = request.POST.get('paragraph1', '')
            if request.POST.get('delete_pic1'):
                residential_service.pic1.delete(save=False)
            if request.FILES.get('pic1'):
                residential_service.pic1 = request.FILES.get('pic1')
            
            residential_service.paragraph_headline2 = request.POST.get('paragraph_headline2', '')
            residential_service.paragraph2 = request.POST.get('paragraph2', '')
            if request.POST.get('delete_pic2'):
                residential_service.pic2.delete(save=False)
            if request.FILES.get('pic2'):
                residential_service.pic2 = request.FILES.get('pic2')
            
            residential_service.paragraph_headline3 = request.POST.get('paragraph_headline3', '')
            residential_service.paragraph3 = request.POST.get('paragraph3', '')
            if request.POST.get('delete_pic3'):
                residential_service.pic3.delete(save=False)
            if request.FILES.get('pic3'):
                residential_service.pic3 = request.FILES.get('pic3')
            
            general_info.save()
            residential_service.save()            
            progress.has_residential_services = True
            progress.save()

            use_help_message = False
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_residential',
         'use_help_message':use_help_message,
         'help_message':RESIDENTIAL_HELP_MESSAGE,
         'residential_service':residential_service,
         'progress':progress,
         'has_residential_page':general_info.has_residential_page,
    }  
    return render(request, 'interface/residential.html', context)

@login_required
def interface_comercial(request):
    PAGE_NAME = "Commercial Services"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        comercial_service = Comercial_Service.objects.get(site__id__exact=get_current_site(request).id)
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (comercial_service.user != user or progress.user != user or general_info.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            if request.POST.get('has_comercial') == 'on':
                general_info.has_comercial_page = True 
            else:
                general_info.has_comercial_page = False 
            comercial_service.paragraph_headline1 = request.POST.get('paragraph_headline1', '')
            comercial_service.paragraph1 = request.POST.get('paragraph1', '')
            if request.POST.get('delete_pic1'):
                comercial_service.pic1.delete(save=False)
            if request.FILES.get('pic1'):
                comercial_service.pic1 = request.FILES.get('pic1')
            
            comercial_service.paragraph_headline2 = request.POST.get('paragraph_headline2', '')
            comercial_service.paragraph2 = request.POST.get('paragraph2', '')
            if request.POST.get('delete_pic2'):
                comercial_service.pic2.delete(save=False)
            if request.FILES.get('pic2'):
                comercial_service.pic2= request.FILES.get('pic2')
            
            comercial_service.paragraph_headline3 = request.POST.get('paragraph_headline3', '')
            comercial_service.paragraph3 = request.POST.get('paragraph3', '')
            if request.POST.get('delete_pic3'):
                comercial_service.pic3.delete(save=False)
            if request.FILES.get('pic3'):
                comercial_service.pic3 = request.FILES.get('pic3')
            
            general_info.save()
            comercial_service.save()            
            
            progress.has_comercial_services = True
            progress.save()

            use_help_message = False
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_comercial',
         'use_help_message':use_help_message,
         'help_message':COMERCIAL_HELP_MESSAGE,
         'comercial_service':comercial_service,
         'progress':progress,
         'has_comercial_page':general_info.has_comercial_page,
    }  
    return render(request, 'interface/commercial.html', context)

@login_required
def interface_other_services(request):
    PAGE_NAME = "Other Services"

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        other_services = Other_Services.objects.get(site__id__exact=get_current_site(request).id)
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (other_services.user != user or progress.user != user or general_info.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            if request.POST.get('has_other_services') == 'on':
                general_info.has_other_services_page = True 
            else:
                general_info.has_other_services_page = False 
    
            other_services.service_headline1 = request.POST.get('service_headline1', '')
            other_services.service1 = request.POST.get('service1', '')
            if request.POST.get('delete_pic1'):
                other_services.pic1.delete(save=False)
            if request.FILES.get('pic1'):
                other_services.pic1 = request.FILES.get('pic1')
            
            other_services.service_headline2 = request.POST.get('service_headline2', '')
            other_services.service2 = request.POST.get('service2', '')
            if request.POST.get('delete_pic2'):
                other_services.pic1.delete(save=False)
            if request.FILES.get('pic2'):
                other_services.pic1 = request.FILES.get('pic2')
            
            other_services.service_headline3 = request.POST.get('service_headline3', '')
            other_services.service3 = request.POST.get('service3', '')
            if request.POST.get('delete_pic3'):
                other_services.pic3.delete(save=False)
            if request.FILES.get('pic3'):
                other_services.pic3 = request.FILES.get('pic3')
            
            other_services.service_headline4 = request.POST.get('service_headline4', '')
            other_services.service4 = request.POST.get('service4', '')
            if request.POST.get('delete_pic4'):
                other_services.pic4.delete(save=False)
            if request.FILES.get('pic4'):
                other_services.pic1 = request.FILES.get('pic4')
            
            other_services.service_headline5 = request.POST.get('service_headline5', '')
            other_services.service5 = request.POST.get('service5', '')
            if request.POST.get('delete_pic5'):
                other_services.pic5.delete(save=False)
            if request.FILES.get('pic5'):
                other_services.pic5 = request.FILES.get('pic5')
            
            general_info.save()
            other_services.save()            
            
            progress.has_other_services = True
            progress.save()

            use_help_message = False
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_other',
         'use_help_message':use_help_message,
         'help_message':OTHER_HELP_MESSAGE,
         'other_services':other_services,
         'progress':progress,
         'has_other_services_page':general_info.has_other_services_page,
    }  
    return render(request, 'interface/other.html', context)

@login_required
def interface_our_people(request):
    PAGE_NAME = "Our People"

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        our_people = Our_People.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (progress.user != user or progress.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')
    
    use_help_message = True 
    if request.POST:
        try:
            our_people.title1 = request.POST.get('title1', '')
            our_people.text1 = request.POST.get('text1', '')
            if request.POST.get('delete_pic1'):
                our_people.pic1.delete(save=False)
            if request.FILES.get('pic1'):
                our_people.pic1 = request.FILES.get('pic1')
            
            our_people.title2 = request.POST.get('title2', '')
            our_people.text2= request.POST.get('text2', '')
            if request.POST.get('delete_pic2'):
                our_people.pic2.delete(save=False)
            if request.FILES.get('pic2'):
                our_people.pic2 = request.FILES.get('pic2')
            
            our_people.title3 = request.POST.get('title3', '')
            our_people.text3 = request.POST.get('text3', '')
            if request.POST.get('delete_pic3'):
                our_people.pic3.delete(save=False)
            if request.FILES.get('pic3'):
                our_people.pic3 = request.FILES.get('pic3')
            
            our_people.title4 = request.POST.get('title4', '')
            our_people.text4 = request.POST.get('text4', '')
            if request.POST.get('delete_pic4'):
                our_people.pic4.delete(save=False)
            if request.FILES.get('pic4'):
                our_people.pic4 = request.FILES.get('pic4')
            
            our_people.title5 = request.POST.get('title5', '')
            our_people.text5 = request.POST.get('text5', '')
            if request.POST.get('delete_pic5'):
                our_people.pic5.delete(save=False)
            if request.FILES.get('pic5'):
                our_people.pic5 = request.FILES.get('pic5')
            
            our_people.title6 = request.POST.get('title6', '')
            our_people.text6 = request.POST.get('text6', '')
            if request.POST.get('delete_pic6'):
                our_people.pic6.delete(save=False)
            if request.FILES.get('pic6'):
                our_people.pic6 = request.FILES.get('pic6')
            
            our_people.title7 = request.POST.get('title7', '')
            our_people.text7 = request.POST.get('text7', '')
            if request.POST.get('delete_pic7'):
                our_people.pic7.delete(save=False)
            if request.FILES.get('pic7'):
                our_people.pic7 = request.FILES.get('pic7')
            
            our_people.title8 = request.POST.get('title8', '')
            our_people.text8 = request.POST.get('text8', '')
            if request.POST.get('delete_pic8'):
                our_people.pic8.delete(save=False)
            if request.FILES.get('pic8'):
                our_people.pic8 = request.FILES.get('pic8')
            
            our_people.title9 = request.POST.get('title9', '')
            our_people.text9 = request.POST.get('text9', '')
            if request.POST.get('delete_pic9'):
                our_people.pic9.delete(save=False)
            if request.FILES.get('pic9'):
                our_people.pic9 = request.FILES.get('pic9')
            
            our_people.title10 = request.POST.get('title10', '')
            our_people.text10 = request.POST.get('text10', '')
            if request.POST.get('delete_pic10'):
                our_people.pic10.delete(save=False)
            if request.FILES.get('pic10'):
                our_people.pic10 = request.FILES.get('pic10')
           
             
            our_people.save()            
            progress.has_our_people = True
            progress.save()

            use_help_message = False
            messages.success(request, PAGE_UPDATED_TEMPLATE)
            
        except:
		      messages.warning(request, SAVE_EXCEPTION)

    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_our_people',
         'use_help_message':use_help_message,
         'help_message':OUR_PEOPLE_HELP_MESSAGE,
         'progress':progress,
         'our_people':our_people,
    }  
    return render(request, 'interface/our_people.html', context)

@login_required
def interface_success_stories(request):
    PAGE_NAME = "Testimonials"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404
    
    if not user.is_superuser and (success_stories.user != user or progress.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
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
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_success_stories',
         'use_help_message':use_help_message,
         'help_message':'This is the Testimonial Page Help Message',
         'success_stories':success_stories,
         'progress':progress,
    }  
    return render(request, 'interface/success_stories.html', context)
   
@login_required
def interface_seo_tools(request):
    PAGE_NAME = "SEO Tool"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        index = Index.objects.get(site__id__exact=get_current_site(request).id)
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
        residential_service = Residential_Service.objects.get(site__id__exact=get_current_site(request).id)
        comercial_service = Comercial_Service.objects.get(site__id__exact=get_current_site(request).id)
        other_services = Other_Services.objects.get(site__id__exact=get_current_site(request).id)
        about = About.objects.get(site__id__exact=get_current_site(request).id)
        why_us = Why_Us.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and (services.user != user or progress.user != user):
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:

            general_info.portfolio_meta_description = request.POST.get('portfolio_description', '')            
            general_info.contact_meta_description = request.POST.get('contact_description', '')            
            general_info.meta_title = request.POST.get('meta_title', '')
            general_info.save()

            index.meta_description = request.POST.get('index_description', '')            
            index.save()
            
            services.meta_description = request.POST.get('services_description', '')            
            services.save()

            progress.has_seo_tools = True
            progress.save()
            
            residential_service.meta_description = request.POST.get('residential_description', '')            
            residential_service.save()
            
            comercial_service.meta_description = request.POST.get('commercial_description', '')            
            comercial_service.save()
            
            other_services.meta_description = request.POST.get('other_description', '')            
            other_services.save()
            
            about.meta_description = request.POST.get('about_description', '')            
            about.save()
            
            why_us.meta_description = request.POST.get('why_us_description', '')            
            why_us.save()

            use_help_message = False
            messages.success(request, PAGE_UPDATED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_seo_tools',
         'use_help_message':use_help_message,
         'help_message':SEO_TOOLS_HELP_MESSAGE,
         'meta_title':general_info.meta_title,
         'contact_description':general_info.contact_meta_description,
         'portfolio_description':general_info.portfolio_meta_description,
         'index_description':index.meta_description,
         'services_description':services.meta_description,
         'residential_description':residential_service.meta_description,
         'commercial_description':comercial_service.meta_description,
         'other_description':other_services.meta_description,
         'why_us_description':why_us.meta_description,
         'about_description':about.meta_description,
         'services':services,
         'progress':progress,
    }  
    return render(request, 'interface/seo_tools.html', context)

@login_required
def interface_add_portfolio(request):
    PAGE_NAME = "Add Portfolio"
    MAX_NUM_PICS = 42

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        num_pics = Portfolio_Pic.objects.filter(site__id__exact=get_current_site(request).id).count()
    except:
        raise Http404

    if not user.is_superuser and progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
            if (num_pics + 1) > MAX_NUM_PICS:
                raise Exception()

            valid_pic_type = True 
            pic_type = request.POST.get('pic_type', '')
            if (pic_type != Portfolio_Pic.INTERRIOR_PIC and
                pic_type != Portfolio_Pic.EXTERRIOR_PIC and
                pic_type != Portfolio_Pic.COMERCIAL_PIC and
                pic_type != Portfolio_Pic.OTHER_PIC and
                pic_type != Portfolio_Pic.WORK_PIC):
                
                valid_pic_type = False
                messages.warning(request, PORTFOLIO_NO_TYPE_MESSAGE)
                  
            if not request.FILES.get('pic'):
                messages.warning(request, PORTFOLIO_NO_PIC_MESSAGE)

            if valid_pic_type and request.FILES.get('pic'):
                new_pic = Portfolio_Pic(user = user,
                                        site = Site.objects.get_current(),
                                        pic_type = request.POST.get('pic_type', ''),                                   
                                        thumb = request.FILES.get('pic'),
                                        pic = request.FILES.get('pic'),
                )
                new_pic.save()
               
                progress.has_portfolio = True
                progress.save()
                use_help_message = False
                messages.success(request, PORTFOLIO_ADDED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_add_portfolio',
         'use_help_message':use_help_message,
         'help_message':ADD_PORTFOLIO_HELP_MESSAGE,
         'MAX_NUM_PICS':MAX_NUM_PICS,
         'PIC_TYPE_CHOICES':Portfolio_Pic.PIC_TYPE_CHOICES,
         'num_pics':num_pics,
         'progress':progress,
    }  
    return render(request, 'interface/add_portfolio.html', context)

@login_required
def interface_billing(request):
    PAGE_NAME = "Billing Settings"
    user = request.user

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        billing = Billing.objects.get(user=user)
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    customer = get_customer(billing.stripe_id)
    update_stripe_email(user, customer)
    
    website_subscription = get_current_subscription(billing, customer) 
 
    if not is_subscription_canceled(website_subscription):
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        general_info.is_website_active = True
        general_info.save()  
 
    if is_subscription_unpaid(website_subscription):
        messages.warning(request, UNPAID_SUBSCRIPTION)

    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'PUB_KEY':PUB_KEY,
         'active_page':'admin_billing',
         'use_help_message':False,
         'has_card':customer['default_card'],
         'is_website_switched_on':is_subscription_on(website_subscription),
         'BIZWIGGLE_EMAIL':BIZWIGGLE_INFO['email'],
         'BIZWIGGLE_PHONE':BIZWIGGLE_INFO['phone'],
         'customer':customer,
         'website_subscription': website_subscription,
         'card':get_default_card(customer),
         'progress':progress,
         'display_trial':billing.display_trial_period,
    } 
    if website_subscription != '':
        context['current_period_end'] = end_subscription_datetime(website_subscription.current_period_end)
        context['trial_end'] = end_subscription_datetime(website_subscription.trial_end)
    return render(request, 'interface/billing.html', context)

@login_required
def interface_add_credit_card(request):
    user = request.user
    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        billing = Billing.objects.get(user=user)
    except:
        raise Http404

    if progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')
 
    if 'stripeToken' in request.POST:
        token = request.POST.get('stripeToken', '')   
        customer = get_customer(billing.stripe_id)
        try:
            new_card = customer.cards.create(card=token)
            if customer.default_card:
                customer.default_card = new_card
            customer.save()    
        except stripe.error.CardError, e:
            body = e.json_body
            err = body['error']
            messages.warning(request, err['message'])
            return redirect('admin_billing')
             

        subscription_messages = {} 
        if not get_current_subscription(billing, customer):
            subscription_messages = create_new_subscription(billing, customer)
            messages.success(request, CREDIT_CARD_UPDATED)

        if subscription_messages.has_key('warning'):
            subscription_messages.warning(request, subscription_messages['warning'])
        if subscription_messages.has_key('success'):
            messages.success(request, subscription_messages['success']) 

    return redirect('admin_billing')

@login_required
def interface_process_service_options(request):
    user = request.user
    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        billing = Billing.objects.get(user=user)
    except:
        raise Http404

    if progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')
 
    customer = get_customer(billing.stripe_id)
    website_subscription = get_current_subscription(billing, customer)    
    is_subscription_active = is_subscription_on(website_subscription)

    if 'website_switch' in request.POST:
        website_switch = request.POST.get('website_switch', '')
        if website_switch == 'on' and not is_subscription_active:
            subscription_messages = create_new_subscription(billing, customer, subscription=website_subscription)         
 
            if subscription_messages.has_key('warning'):
                subscription_messages.warning(request, subscription_messages['warning'])
            if subscription_messages.has_key('success'):
                messages.success(request, subscription_messages['success']) 

 
        elif website_switch == 'off' and is_subscription_active:
            turn_off_subscription(customer, billing)
            messages.success(request, WEBSITE_CANCELED)
            
            EMAIL_BODY = ''.join([user.email, 'has shut off web service for ', settings.SITE_NAME])
            send_mail('Important - Customer Shutoff Service', EMAIL_BODY, BIZWIGGLE_INFO['email'], 
                    [BIZWIGGLE_INFO['email'] ], fail_silently=True
            )

    return redirect('admin_billing')

@login_required
def interface_edit_portfolio(request):
    PAGE_NAME = "Edit Portfolio"

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        portfolio_pics = Portfolio_Pic.objects.filter(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')


    use_help_message = True 
    if request.POST:
        try:
            pic_to_delete = Portfolio_Pic.objects.get(pk= int(request.POST.get('id', '')))
            pic_to_delete.delete()
            use_help_message = False
            messages.success(request, PIC_DELETED_TEMPLATE)
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_edit_portfolio',
         'use_help_message':use_help_message,
         'help_message':EDIT_PORTFOLIO_HELP_MESSAGE if portfolio_pics.count() > 0 else NO_PORTFOLIO_PICS_HELP_MESSAGE,
         'portfolio_pics':portfolio_pics,
         'progress':progress,
    }  
    return render(request, 'interface/edit_portfolio.html', context)

@login_required
def interface_change_password(request):
    PAGE_NAME = "Change Password"

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')


    use_help_message = True 
    if request.POST:
        try:
            current_password = request.POST.get('current_password', '') 
            check_user = authenticate(email=user.email, password=current_password) 
            if not check_user is None:
                new_password = request.POST.get('new_password', '')
                user.set_password(new_password)
                user.save()

                messages.success(request, CHANGE_PASSWORD_SUCCESS)
            else:
                messages.warning(request, CURRENT_PASSWORD_FAILED)

            use_help_message = False
        except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_change_password',
         'use_help_message':use_help_message,
         'help_message':CHANGE_PASSWORD_HELP_MESSAGE,
         'progress':progress,
    }  
    return render(request, 'interface/password.html', context)

def interface_login(request):
    if request.POST:
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                error_message = "".join(["This account is currently inactive.",
                                         " Please call %s or email %s",
                                         " to reactivate this account."])
                error_message = error_message % (BIZWIGGLE_INFO['phone'], BIZWIGGLE_INFO['email'])
                messages.error(request, "error message")
        else:
            error_message = "Invalid email address or password"
            messages.error(request, error_message)
    
    context = {
        'page_title':'My Website Login',
        'page_description':'Enter page descrption here'
    }

    return render(request, 'interface/login/login.html', context)

def interface_forgot_password(request):
    if request.POST:
        message = "".join(["If you are still having trouble, ",
                           "please contact customer support at %s  or email %s."])
        messages.warning(request, message % (BIZWIGGLE_INFO['phone'], BIZWIGGLE_INFO['email']))
        try: 
            user = MyUser.objects.get(email=request.POST.get('email', False))
            phone_number = request.POST.get('phone', False)
      
            progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
            if progress.user != user:
                raise Exception
            
            phone_number = re.sub(r'\W+', '', phone_number)            
            if phone_number != user.phone_number:
                raise Exception                

            new_password = str(uuid.uuid4())[0:20]
            user.set_password(new_password)
            user.save()
            email_subject = "My Website Login from Bizwiggle"
            email_message = "".join(["You have successfully created a new password.  Please login at",
                                     " %s/admin/ with your new password %s.  You can change your password",
                                     " by clicking your name in the top right and selecting account settings.",
            ])
            email_message = email_message % ( get_current_site(request), new_password)
            user.email_user(email_subject, email_message)
            return redirect('admin_login')

        except:
            return redirect('admin_login')
            
    context = {
        'page_title':'My Website Reset Password',
        'page_description':'page description goes here',
    }

    return render(request, 'interface/login/forgot_password.html', context) 

@login_required
def interface_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def interface_contact(request):
    PAGE_NAME = "Contact Bizwiggle"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404
    
    if not user.is_superuser and progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    if request.POST:
       try:
            message = request.POST.get('message', '')
            if message:
                email_subject = "Important - help request from user"
                email_message = "".join(['user:  ', user.email, '\n',
                                         'phone: ', user.phone_number, '\n\n',
                                          message
                ])
                send_mail(email_subject, email_message, BIZWIGGLE_INFO['email'],
                          [ BIZWIGGLE_INFO['email'] ], fail_silently=False)          
                messages.success(request, MESSAGE_SENT_SUCCESS)
       except:
            messages.warning(request, SAVE_EXCEPTION)
   
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_contact',
         'BIZWIGGLE_PHONE':BIZWIGGLE_INFO['phone'],
         'use_help_message':False,
         'progress':progress,
    }   

    return render(request, 'interface/contact.html', context)

@login_required
def interface_faq(request):
    PAGE_NAME = "FAQ"

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if not user.is_superuser and progress.user != user: 
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')
    
    context = { 
         'page_title': Template(PAGE_TITLE_TEMPLATE).substitute(page_name=PAGE_NAME),
         'page_description':'Enter page descrption here',
         'active_page':'admin_faq',
         'use_help_message':False,
         'progress':progress,
    }

    return render(request, 'interface/faq.html', context)

def create_user_objects(request):
    user = request.user
    try:
        billing = Billing.objects.get(user=user)
    except:
        stripe.api_key = SECRET_KEY
        customer_description = "Painting Website for %s" % get_current_site(request) 
        stripe_customer = stripe.Customer.create(
                              description=customer_description,
                              email=user.email,
        )
        billing = Billing(user=user,
                      stripe_id=stripe_customer.id,        
        )
        billing.save()
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        general_info = General_Info(user=user,
                           site=Site.objects.get_current(),
        )
        general_info.save()

    try:
        index = Index.objects.get(site__id__exact=get_current_site(request).id)
    except:
        index = Index(user=user,
                    site=Site.objects.get_current(),
        )
        index.save()

    try:
        success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
    except:
        success_stories = Success_Stories(user=user,
                    site=Site.objects.get_current(),
        )
        success_stories.save()

    try:
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
    except:
        services = Services(user=user,
                       site=Site.objects.get_current(),
        )
        services.save()
    
    try:
        residential_service = Residential_Service.objects.get(site__id__exact=get_current_site(request).id)
    except:
        residential_service = Residential_Service(user=user,
                       site=Site.objects.get_current(),
        )
        residential_service.save()

    try:
        comercial_service = Comercial_Service.objects.get(site__id__exact=get_current_site(request).id)
    except:
        comercial_service = Comercial_Service(user=user,
                                site=Site.objects.get_current(),
        )
        comercial_service.save()

    try:
        other_services = Other_Services.objects.get(site__id__exact=get_current_site(request).id)
    except:
        other_services = Other_Services(user=user,
                             site=Site.objects.get_current(),
        )
        other_services.save()
    
    try:
        why_us = Why_Us.objects.get(site__id__exact=get_current_site(request).id)
    except:
        why_us = Why_Us(user=user,
                     site=Site.objects.get_current(),
        )
        why_us.save()

    try:
        about = About.objects.get(site__id__exact=get_current_site(request).id)
    except:
        about = About(user=user,
                    site=Site.objects.get_current(),
        )
        about.save()

    try:
        our_people = Our_People.objects.get(site__id__exact=get_current_site(request).id)
    except:
        our_people = Our_People(user=user,
                         site=Site.objects.get_current(),
        )
        our_people.save()
        
    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        progress = Progress(user=user,
                       site=Site.objects.get_current(),
        )
        progress.save()
    
