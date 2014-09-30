import datetime
import time
import stripe

from django.conf import settings

from painting.stripe_info import SECRET_KEY
from interface.models import Billing
from interface.user_messages import ACCOUNT_NOW_ACTIVE, WEBSITE_ACTIVE 

def get_customer(stripe_id):
    stripe.api_key = SECRET_KEY
    return stripe.Customer.retrieve(stripe_id)

def update_stripe_email(user, customer):
    if user.email != customer.email:
        customer.email = user.email
        customer.save()

def get_current_subscription(billing, customer):
    current_subscription = ""
    for subscription in customer.subscriptions.data:
        if subscription.id == billing.stripe_id_website_sub:
            current_subscription = subscription
            break
    return current_subscription

def get_default_card(customer):
    card = ''
    if customer.default_card:
        card = customer.cards.retrieve(customer.default_card)
    return card

def is_subscription_canceled(subscription):
    return (subscription != "" and subscription.status == 'canceled')

def is_subscription_on(subscription):
    return (subscription != "" and subscription.status != 'canceled' and not subscription.cancel_at_period_end)

def is_subscription_unpaid(subscription):
    return (subscription != "" and subscription.status == 'unpaid')

def end_subscription_datetime(timestamp):
    end_date = ''
    if timestamp:
        end_date = datetime.datetime.fromtimestamp(timestamp)
    return end_date

def create_new_subscription(billing, customer, **kwargs):
    HOURS_IN_DAY = 24
    MIN_IN_HOUR = 60
    SEC_IN_MIN = 60    


    messages = {}
    try:
        # first time adding payment - give trial
        if not billing.stripe_id_website_sub:
            trial_days = settings.TRIAL_LENGTH
            secconds_of_trial = (trial_days * HOURS_IN_DAY * MIN_IN_HOUR * SEC_IN_MIN)
            end_trial_timestamp = int(time.time() + secconds_of_trial)
            new_subscription = customer.subscriptions.create(plan=settings.STRIPE_PLAN, trial_end=end_trial_timestamp)
            messages['success'] = WEBSITE_ACTIVATED 

        # reactivating website that was turned off - trial until current subscription end
        elif 'subscription' in kwargs: 
            end_subscription_timestamp = kwargs['subscription'].current_period_end
            customer.subscriptions.retrieve(billing.stripe_id_website_sub).delete()
            new_subscription = customer.subscriptions.create(plan=settings.STRIPE_PLAN, trial_end=end_subscription_timestamp)
            messages['success'] = WEBSITE_ACTIVATED

        # no current subscription
        else:
            new_subscription = customer.subscriptions.create(plan=settings.STRIPE_PLAN)
            messages['success'] = ACCOUNT_NOW_ACTIVE
        
        update_check_stripe_date(billing.user, new_subscription) 
        customer.save()
        billing.stripe_id_website_sub = new_subscription.id
        billing.save()
    except stripe.error.CardError,e:
        body = e.json_body
        err = body['error']
        messages['warning'] = err['message']
    
    return messages

def update_check_stripe_date(user, subscription):
    user.check_stripe_date = end_subscription_datetime(subscription.current_period_end)
    user.save() 

def turn_off_subscription(customer, billing):
    customer.subscriptions.retrieve(billing.stripe_id_website_sub).delete(at_period_end=True)

