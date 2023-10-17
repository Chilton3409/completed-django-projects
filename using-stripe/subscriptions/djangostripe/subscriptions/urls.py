from django.urls import path
from . import views
app_name = 'subscriptions'
urlpatterns = [
    path('', views.home, name='subscription'),
    path('config/', views.stripe_config),# new for stripe
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),
    path('cancel/', views.cancel),
    path('webhook/', views.stripe_webhook)#new
    

    
    
]