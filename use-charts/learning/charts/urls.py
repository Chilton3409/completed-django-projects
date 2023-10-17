from django.contrib import admin
from django.urls import path, include
from . import views 
app_name = 'charts'
urlpatterns = [

    path('', views.BillsChartView.as_view(), name='index')
]