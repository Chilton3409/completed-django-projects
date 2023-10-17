from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from .models import Income, Expense, Budget
from .serializers import IncomeSerializer, ExpenseSerializer, BudgetSerializer
from rest_framework import status 
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets


#root of api
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
      
        'income': reverse('budget:income-list', request=request, format=format),
        'expense': reverse('budget:expense-list', request=request, format=format),
        'budget': reverse('budget:budget-list', request=request, format=format),
    })


# Create your views here.
#root of api
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsOwnerOrReadOnly]


#now going to write the budget views using class based views
class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        

    

        