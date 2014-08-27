from django import template
from django.template.defaultfilters import stringfilter

from django.core.urlresolvers import reverse

from pages.models import Index, Services, Portfolio_Pic

register = template.Library()

@register.filter
@stringfilter
def slider_pages_link(value): 
    pages = {
        Index.WHY_US:reverse('why-us'),
        Index.SERVICES:reverse('services'),
        Index.RESIDENTIAL:reverse('residential'),
        Index.COMERCIAL:reverse('comercial'),
        Index.OTHER:reverse('other'),
        Index.PORTFOLIO:reverse('portfolio'),
        Index.ABOUT:reverse('about'),
        Index.CONTACT:reverse('contact'),
    }
    try:
        return pages[value]
    except:
        return '#'

@register.filter
@stringfilter
def service_pages_link(value): 
    pages = {
        Services.RESIDENTIAL:reverse('residential'),
        Services.COMERCIAL:reverse('comercial'),
        Services.OTHER:reverse('other'),
    }
    try:
        return pages[value]
    except:
        return '#'

@register.filter
@stringfilter
def isotope(value): 
    isotopes = {
        Portfolio_Pic.INTERRIOR_PIC:'isotope-filter1',
        Portfolio_Pic.EXTERRIOR_PIC:'isotope-filter2',
        Portfolio_Pic.COMERCIAL_PIC:'isotope-filter3',
        Portfolio_Pic.OTHER_PIC:'isotope-filter4',
        Portfolio_Pic.WORK_PIC:'isotope-filter5',
    }
    try:
        return isotopes[value]
    except:
        return ''
