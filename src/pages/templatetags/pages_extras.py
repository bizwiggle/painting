from django import template
from django.template.defaultfilters import stringfilter

from django.core.urlresolvers import reverse

register = template.Library()

@register.filter
@stringfilter
def service_pages_link(value):
    pages = {
        'R':reverse('residential'),
        'C':reverse('comercial'),
        'O':reverse('other'),
        'N':'#'
    }
    return pages[value]
    
