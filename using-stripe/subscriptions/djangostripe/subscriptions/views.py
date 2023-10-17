from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe 
from django.contrib.auth.models import User

from .models import StripeCustomer
# Create your views here.
@login_required
def home(request):
    #below is how to fetch the subscrition and check its status in other apps
    
    try:
         #retrieve the subscription and product
         stripe_customer = StripeCustomer.objects.get(user=request.user)
         stripe.api_key = settings.STRIPE_SECRET_KEY
         subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
         product = stripe.Product.retrieve(subscription.plan.product)
         # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object
         return render(request, 'subscriptions/home.html', {
            'subscription': subscription,
            'product': product,
    })

    except StripeCustomer.DoesNotExist:
         return render(request, 'subscriptions/home.html')
    
   


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    

    #checkout views for stripe

@csrf_exempt
def create_checkout_session(request):
        if request.method == 'GET':
            #this will chnage when pushing to prod
            domain_url = 'http://localhost:8000/'
            stripe.api_key = settings.STRIPE_SECRET_KEY
            try:
                checkout_session = stripe.checkout.Session.create(
                    client_reference_id=request.user.id if request.user.is_authenticated else None,
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url=domain_url + 'cancel/',
                    payment_method_types=['card'],
                    mode='subscription',
                    line_items=[
                        {
                            'price':settings.STRIPE_PRICE_ID,#getting the price of the subscription from stripe
                            'quantity': 1,
                        }
                    ]

                )
                return JsonResponse({'sessionId': checkout_session['id']})
            except Exception as e:
                return JsonResponse({'error': str(e)})
            



#views for canceling and success

@login_required
def success(request):
     return render(request, 'subscriptions/success.html')

@login_required
def cancel(request):
     return render(request, 'subscriptions/cancel.html')

@csrf_exempt
def stripe_webhook(request):
     stripe.api_key = settings.STRIPE_API_KEY
     endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
     payload = request.body
     sig_header = request.Meta['HTTP_STRIPE_SIGNATURE']
     event = None
     
     try:
          event = stripe.Webhook.construct_event(
               payload, sig_header, endpoint_secret
          )
     except ValueError as e:
          return HttpResponse(status=400)
     except stripe.error.SignatureVerificationError as e:
          return HttpResponse(status=400)
     

#handle the checkout complete event
     if event['type'] == 'checkout.session.completed':
          session = event['data']['object']

          client_reference_id = session.get('client_reference_id')
          stripe_customer_id = session.get('customer')
          stripe_subscription_id = session.get('subscription')
          #get the user and creaye a new stripe user
          user = User.objects.get(id=client_reference_id)
          StripeCustomer.objects.create(user=user,
                                        stripeCustomerId=stripe_customer_id,
                                        stripeSubscriptionId=stripe_subscription_id,)
          print(user.username + ' just subscribed')
     return HttpResponse(status=200)
         
