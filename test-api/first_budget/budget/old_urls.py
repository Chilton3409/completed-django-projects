from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
app_name = 'budget'
urlpatterns = [
    path('', views.api_root),
    path('income/', views.IncomeList.as_view(), name='income-list'),
    path('income/<uuid:pk>/', views.IncomeDetail.as_view(), name='income-detail'),
    path('expense/', views.ExpenseList.as_view(), name='expense-list'),
    path('expense/<uuid:pk>/', views.ExpenseDetail.as_view(), name='expense-detail'),

    #refactor because of class based views
    path('budget/', views.BudgetList.as_view(), name='budget-list'),
    path('budget/<uuid:pk>/', views.BudgetDetail.as_view(), name='budget-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')




    

]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)




    

