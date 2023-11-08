from django.db import models
import uuid 
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from math import ceil
import math



# Create your models here.
#todo's add a debt and assets model
class Debt(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, help_text="Enter debt type or bill type")
    amount = models.IntegerField(help_text="enter amount owed")
    creation_date = models.DateField(auto_now_add=True)
    deadline = models.DateField(default=timezone.now())
    

    class Meta:
        pass

    def __str__(self):
        return self.name
    def get_absolute_url(self):
         return reverse("budget:debt-detail", args=[str(self.id)])
    
    def month_counter(self):
        if self.deadline is not None:
            months_diff = ceil((self.deadline - self.creation_date).days / 30)
            return months_diff
        
    def payment_maker(self):
        if self.deadline is not None:
            months_diff = ceil((self.deadline - self.creation_date).days / 30)
            if months_diff != 0:
                how_much_each_month = self.amount / months_diff
                how_much_each_month = int(how_much_each_month)
            else:
                how_much_each_month = self.amount / 1
            return how_much_each_month
            


    
#class representing a single savings goal
class SavingsGoal(models.Model):
     id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
     name = models.CharField(max_length=100, help_text="Name your savings goal.")

     goal = models.IntegerField(help_text="Savings Goal",)
     creation_date = models.DateField(auto_now_add=True)
     deadline = models.DateField(default=timezone.now(), help_text="When do you want to reach your saving's goal?")

    
     class Meta:
         pass
     def __str__(self):
         return f'{self.name}'
     def get_absolute_url(self):
         return reverse("budget:savings-goals-detail", args=[str(self.id)])
     def get_total(self):
         total = self.goal
         return total
     
     def deadline_reached_month(self):
        if self.deadline is not None:
            months_diff = ceil((self.deadline - self.creation_date).days / 30)
            return months_diff
    
     def how_much_each_month(self):
        if self.deadline is not None:
            months_diff = ceil((self.deadline - self.creation_date).days / 30)
            if months_diff != 0:
                how_much_each_month = self.goal / months_diff
                how_much_each_month = math.ceil(how_much_each_month)
            else:
                how_much_each_month = self.goal / 1
                how_much_each_month = int(how_much_each_month)
            return how_much_each_month
     def goal_reached(self):
         if self.goal == 0:
            return "goal has been reached!!!"
         else:
             return self.goal

         
    
#class representing a single budget
class Budget(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, help_text="Use the tab keys for quick completion.")
    expenses = models.IntegerField(help_text="Enter  0 if recording income")
    income = models.IntegerField(help_text="Enter 0 if recording an expense")
    creation_date = models.DateField(auto_now_add=True)
    is_monthly = models.BooleanField(default=False, help_text="Is this income/expense a weekly fixed or one time event?")
    is_weekly = models.BooleanField(default=False, help_text="Is this income/expense a weekly fixed or one time event?")

    class Meta:
        pass
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse("budget:budget_detail", args=[str(self.id)])
    
    def get_total(self):
        #gets totoal for a single row, or model instance
        total = self.income - self.expenses
        return total
    

    def after_tax(self):
        total = self.income - self.expenses
        after_tax = total - total * .10
        if after_tax > 0:
            return int(after_tax)
        else:
            message = "No taxable income"
            return message
    
    def savings(self):
        total = self.income - self.expenses
        savings =  int(total *.20)
        return savings
    
    def yearly_income(self):
        if self.expenses is not None:
            if self.is_monthly == True:
                yearly_income = self.income * 12
                return yearly_income
            else:
                return 0
        
    def yearly_expenses(self):
        if self.expenses is not None:
            if self.is_monthly == True:

                cost = self.expenses * 12
                yearly = int(cost)
                return yearly
            else:
                return 0
            
    def yearly_net(self):
        if self.income is not None:
            if self.is_monthly == True:
                if self.expenses is not None:
                    if self.is_monthly == True:
                        yearly_income = self.income * 12
                        yearly_expenses = self.expenses * 12

                        yearly_net = yearly_income - yearly_expenses
                        
                        return yearly_net
                    
                    else:
                        return 0
            
    def yearly_tax(self):
        if self.income is not None:
            yearly_income = self.income * 12

            yearly_tax = yearly_income * .10
            yearly_tax = int(yearly_tax)
            return yearly_tax
        else:
            return 0
        
        
    
    def debt(self):
        total = self.income - self.expenses
        amount = total * .10
        if amount > 0:
            return round(amount)
        else: 
            message = "expenses exceed income"
            return message
        
    # calc percentage of expenses
    def totalpercent(self):
        if self.income is not None:
            if self.expenses is not None:
                total = self.income - self.expenses

                percent = total / self.expenses
                
                return percent
    
    
class BusinessMessage(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)
        email = models.EmailField(primary_key=False, help_text="Enter business email")
        phone = models.IntegerField(null=False, blank=False, help_text="Enter business phone number")
        message = models.TextField(null=True, blank=True, help_text='leave a brief message for clients')
        class Meta:
            ordering = ['email']

        def __str__(self):
            return f'{self.email}'
    
        def get_absolute_url(self):
            pass


