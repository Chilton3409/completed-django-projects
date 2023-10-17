from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
from rest_framework.routers import DefaultRouter
app_name = 'budget'

#create a router and register my viewsets
router = DefaultRouter()
router.register(r'^income$', views.IncomeViewSet,basename='income'),
router.register(r'^expense$', views.ExpenseViewSet, basename='expense'),

router.register(r'^budget$', views.BudgetViewSet, basename="budget"),

#api urls are now determined by the router in place
urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]
format_suffix_patterns(urlpatterns)
