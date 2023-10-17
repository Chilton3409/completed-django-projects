from django.db import models
import uuid 
from django.conf import settings
from django.urls import reverse

# Create your models here.
#going to start wide and then get more specific

class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    id= models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True)
    CHOICES = (
        ('w', 'wage'),
        ('i', 'investments'),
        ('o', 'other'),
    )
    income_type = models.CharField(max_length=1, choices=CHOICES)
    date = models.DateField()
    amount = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.get_income_type_display()}, {self.amount}'
    
    def get_absolute_url(self):
        return reverse("budget:income-detail", args=[str(self.id)])
    
    
class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    id= models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True)
    amount = models.PositiveBigIntegerField()
    TYPES = (
        ('b', 'bill'),
        ('g', 'groceries'),
        ('o', 'other')
    )
    expense_type = models.CharField(max_length=1, choices=TYPES)
    date = models.DateField()

    def __str__(self):
        return f'{self.get_expense_type_display()}, {self.amount}'
    def get_absolute_url(self):
        return reverse("budget:expense-detail", args=[str(self.id)])
    
    
class Budget(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    id= models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True)
    name = models.CharField(max_length=100)
    income = models.ManyToManyField(Income)
    expense = models.ManyToManyField(Expense)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("budget:budget-detail", args=[str(self.id)])
    
    
 
class BudgetInstance(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4)
    CHOICES = (
        ('d', 'debt repayment'),
        ('s', 'savings goal'),
        ('n', 'neccessities'),
        ('w', 'wants')
    )
    budget_type = models.CharField(max_length=1, choices=CHOICES)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_budget_type_display()}'
    