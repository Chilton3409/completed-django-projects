from django.urls import path 


from django.views import generic
from . import views

from django.utils.translation import gettext_lazy as _
app_name='users'
urlpatterns= [
    path('MyProfile/', views.UserListView.as_view(), name='my-profile'),
    path('MyProfile/<int:pk>/Update/', views.UserUpdateView.as_view(), name='user-update'),
    path('MyProfile/<int:pk>/Delete/', views.UserDeleteView.as_view(), name='user-delete'),
]