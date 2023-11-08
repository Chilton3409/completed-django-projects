from django.urls import path 
from . import views
app_name = 'budget'
urlpatterns = [
path('/', views.index, name='home'),
path('budget/', views.BudgetListView.as_view(), name='budget_list'),
path('budgetDetails/<uuid:pk>/', views.BudgetDetailView.as_view(), name='budget_detail'),
path('budgetCreate/', views.BudgetCreateView.as_view(), name='budget_create'),
path('budgetUpdate/<uuid:pk>/update/', views.BudgetUpdateView.as_view(), name='budget_update'),
path('budgetDelete/<uuid:pk>/delete/', views.BudgetDeleteView.as_view(), name='budget_delete'),
path('budget/budgetResults', views.SearchResultsList.as_view(), name='search'),

path('LeaveMessage/', views.BusinessCreateView.as_view(), name='business_create'),

#begin savings goals views
path('savings-goals/', views.SavingsGoalListView.as_view(), name='savings-goals'),
path('savings-goals-detail/<uuid:pk>/', views.SavingsGoalsDetailView.as_view(), name='savings-goals-detail'),

#begin savings goal crud urls
path('savings-goals-create/', views.SavingsGoalCreate.as_view(), name='savings-goals-create'),
path('savings-goals/<uuid:pk>/update/', views.SavingsGoalUpdate.as_view(), name='savings-goals-update'),
path('savings-goals-delete/<uuid:pk>/delete/', views.SavingsGoalDelete.as_view(), name='savings-goals-delete'),

#begin debt urls
path('debt/', views.DebtListView.as_view(), name='debt-list'),
path('debt/<uuid:pk>/detail/', views.DebtDetailView.as_view(), name='debt-detail'),

#begin debt crud views
path('debt-create/', views.DebtCreate.as_view(), name='debt-create'),
path('debt-update/<uuid:pk>/update/', views.DebtUpdate.as_view(), name='debt-update'),
path('debt-delete/<uuid:pk>/delete/', views.DebtDelete.as_view(), name='debt-delete'),

#----------rest api views-------
path('debt-api-list/', views.debt_list),
path('debt-api-detail/', views.debt_detail),




]
