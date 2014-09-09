#for testing only
from django.http import HttpResponse, Http404

from string import Template

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.contrib import messages
from django.contrib.sites.models import Site

from painting.constants import STATES

from pages.models import (Why_Us, Success_Stories, About, Services, Residential_Service,
    Comercial_Service, Other_Services, General_Info, Our_People, Index, Portfolio_Pic
) 

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
    PAGE_NAME = "Business Info"
    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if progress.user != user or general_info.user != user:
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
           
            if request.POST.get('logo'):
                general_info.logo.delete(save=False)
                general_info.logo_small.delete(save=False)
            if request.FILES.get('hello_pic'):
                general_info.logo = request.FILES.get('logo')
                general_info.logo_small = request.FILES.get('logo')
            
            general_info.why_us_brief = request.POST.get('why_us_brief', '')
            general_info.banner_text = request.POST.get('banner_text', '')
            
            general_info.save()
            
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

    if index.user != user or progress.user != user:
        messages.warning(request, INCORRECT_USER_SITE_LOGIN) 
        return redirect('admin_login')

    use_help_message = True 
    if request.POST:
        try:
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

    if about.user != user or progress.user != user:
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

    if general_info.user != user or progress.user != user:
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
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        why_us = Why_Us.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if why_us.user != user or progress.user != user:
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
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        services = Services.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if services.user != user or progress.user != user:
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

    if residential_service.user != user or progress.user != user or general_info.user != user:
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

    if comercial_service.user != user or progress.user != user or general_info.user != user:
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

    if other_services.user != user or progress.user != user or general_info.user != user:
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
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        our_people = Our_People.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404

    if progress.user != user or progress.user != user:
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
         'help_message':ADD_PERSON_HELP_MESSAGE,
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
	     # return redirect
        return redirect('admin_login')

    try:
        success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404
    
    if success_stories.user != user or progress.user != user:
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
   

def interface_add_portfolio(request):
    PAGE_NAME = "Add Portfolio"
    MAX_NUM_PICS = 42

    user = request.user
    if not user.is_active:
        messages.warning(request, INACTIVE_ACCOUNT_MSG) 
	     # should redirect to billing page 
        return redirect('admin_login')

    try:
        progress = Progress.objects.get(site__id__exact=get_current_site(request).id)
        num_pics = Portfolio_Pic.objects.filter(site__id__exact=get_current_site(request).id).count()
    except:
        raise Http404

    if progress.user != user:
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

def interface_edit_portfolio(request):
    return HttpResponse('This is the edit for portfolio')
 
def interface_login(request):
    return HttpResponse('This is the login for admin page')
 
