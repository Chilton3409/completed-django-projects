from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from .views import *
class IncomeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Income
        fields = '__all__'


    
    
class ExpenseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Expense
        fields = '__all__'

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
  


    class Meta:
        model = Budget
        fields = '__all__'

  

