import datetime
import stripe

from django.conf import settings
from django.http import Http404
from django.core.mail import send_mail

from painting.constants import DAYS_BETWEEN_BILLING_CHECK, BIZWIGGLE_INFO

from painting.stripe_info import PUB_KEY, SECRET_KEY
from interface.models import Billing

def check_user_status(general_info):
    user = general_info.user
    if user.check_stripe_date < datetime.date.today():
        try: 
            billing = Billing.objects.get(user=user)
        except:
            pass

        stripe.api_key = SECRET_KEY
        try:
            customer = stripe.Customer.retrieve(billing.stripe_id)
            web_subscription = customer.subscriptions.retrieve(billing.stripe_id_website_sub)
             
            if web_subscription.status == 'canceled':
                general_info.is_website_active = False
                general_info.save()
                send_canceled_email(user)
            else:
                billing_check_delta = datetime.timedelta(days=DAYS_BETWEEN_BILLING_CHECK)
                user.check_stripe_date += billing_check_delta
                user.save()
        except:
            general_info.is_website_active = False
            general_info.save()
            send_canceled_email(user)
   
    if not general_info.is_website_active:
        raise Http404
   
def send_canceled_email(user):
    EMAIL_BODY = ''.join([user.email, "'s website has been shutoff for non-payment ", settings.SITE_NAME])
    send_mail('Important - Customer Non-Payment', EMAIL_BODY, BIZWIGGLE_INFO['email'], [BIZWIGGLE_INFO['email'] ], fail_silently=True)
  
