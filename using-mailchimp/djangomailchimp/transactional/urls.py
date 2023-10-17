from django.urls import path

from . import views

app_name = 'transactional'

urlpatterns = [
    path('send/', views.send_view, name='mailchimp-send'),
    
]