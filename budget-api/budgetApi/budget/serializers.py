from rest_framework import serializers
from .models import Debt, SavingsGoal, Budget
from django.utils import timezone
from django.contrib.auth import get_user_model


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['id', 'user', 'name', 'amount', 'creation_date', 'deadline']
        

class UserSerializer(serializers.ModelSerializer):
    debt = serializers.PrimaryKeyRelatedField(many=True, queryset=Debt.objects.all())

    class Meta:
        model = get_user_model()
        fields = '__all__'