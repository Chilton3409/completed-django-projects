from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'social_app'

urlpatterns = [

    path('', views.home, name='home')

    #path('users/', include('users.urls')),
]
