from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from django.core.mail import send_mail
from django.contrib import messages

from painting.constants import BIZWIGGLE_INFO

from pages.models import *
from pages.functions import check_user_status

def index(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        index = Index.objects.get(site__id__exact=get_current_site(request).id)
        success_stories = Success_Stories.objects.get(site__id__exact=get_current_site(request).id)
    except:
        raise Http404
    
    check_user_status(general_info)
    page_title = (general_info.business_name + ' | Index') if (general_info.meta_title == '') else (general_info.meta_title + ' | Index')

    context = {
        'page_title':page_title,
        'page_description':index.meta_description,
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

    check_user_status(general_info)
    page_title = (general_info.business_name + ' | Why Us') if (general_info.meta_title == '') else (general_info.meta_title + ' | Why Us')

    context = {
        'page_title':page_title,
        'page_description':why_us.meta_description,
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
    
    check_user_status(general_info)
    page_title = (general_info.business_name + ' | Services') if (general_info.meta_title == '') else (general_info.meta_title + ' | Services')

    context = {
        'page_title':page_title,
        'page_description':services.meta_description,
        'active':'services',
        'general_info':general_info,
        'services':services,
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
    
    check_user_status(general_info)
    page_title = (general_info.business_name + ' | Residential') if (general_info.meta_title == '') else (general_info.meta_title + ' | Residential Services')

    context = {
        'page_title':page_title,
        'page_description':residential_service.meta_description,
        'active':'residential',
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
    
    check_user_status(general_info)
    page_title = (general_info.business_name + ' | Comercial') if (general_info.meta_title == '') else (general_info.meta_title + ' | Comercial Services')

    context = {
        'page_title':page_title,
        'page_description':comercial_service.meta_description,
        'active':'comercial',
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
    
    check_user_status(general_info)
    page_title = (general_info.business_name + ' | Services') if (general_info.meta_title == '') else (general_info.meta_title + ' | Other Services')

    context = {
        'page_title':page_title,
        'page_description':other_services.meta_description,
        'active':'other',
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
    
    check_user_status(general_info)
    page_title = (general_info.business_name + ' | Portfolio') if (general_info.meta_title == '') else (general_info.meta_title + ' | Our Portfolio')

    has_pic_dict = {}
    for pic_choice in Portfolio_Pic.PIC_TYPE_CHOICES:
        has_pic_dict[pic_choice[0]] = False

    for pic in portfolio_pics:
        has_pic_dict[pic.pic_type] = True

    context = {
        'page_title':page_title,
        'page_description':general_info.portfolio_meta_description,
        'active':'portfolio',
        'general_info':general_info,
        'has_pic_dict':has_pic_dict,
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
    
    check_user_status(general_info)
    page_title = (general_info.business_name + ' | About Us') if (general_info.meta_title == '') else (general_info.meta_title + ' | About Us')

    context = {
        'page_title':page_title,
        'page_description':about.meta_description,
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
    
    check_user_status(general_info)
    page_title = (general_info.business_name + ' | Contact') if (general_info.meta_title == '') else (general_info.meta_title + ' | Contact')

    context = {
        'page_title':page_title,
        'page_description':general_info.contact_meta_description,
        'active':'contact',
        'general_info':general_info,
    }
    return render(request, 'contact.html', context)


def email_handler(request):
    try:
        general_info = General_Info.objects.get(site__id__exact=get_current_site(request).id)
        send_to_email = general_info.email if general_info.email else user.email
    except:
        send_to_email = BIZWIGGLE_INFO['email']
    
    if request.POST:
         message = ''
         if 'message' in request.POST:
             message =  ''.join(['\nmessage:' , request.POST.get('message', '')])

         EMAIL_BODY = ''.join([ 'Lead from website:\n', 
                                '\nname : ', request.POST.get('name', ''),
                                '\nemail: ', request.POST.get('email', ''),
                                '\nphone: ', request.POST.get('phone', ''), 
                                 message, '\n\n',
                                'This message was sent from your Bizwiggle website',                                    
         ])
         EMAIL_SUBJECT = 'Important - Website Lead'   
         from_email = BIZWIGGLE_INFO['email']
         send_mail(EMAIL_SUBJECT, EMAIL_BODY, from_email, [ send_to_email ], fail_silently=True)

   
    if 'next' in request.GET:
        return redirect(request.GET['next'])
    else:
        return redirect('index')
