from django.urls import path 
from . import views
app_name = 'budget'
urlpatterns = [


#----------rest api views-------
path("", views.DebtListAPIView.as_view(), name='debt_list'),

path("update/<int:pk>/", views.UpdateAPIView.as_view(), name="update_debt"),
path("delete/<int:pk>/", views.DebtDetailView.as_view(), name='delete_debt'),

path('users/', views.UserList.as_view(), name='user-list'),
path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),





]
