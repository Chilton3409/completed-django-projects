from django.shortcuts import render
from .models import Budget, BusinessMessage, SavingsGoal, Debt
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.db.models import Q
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Permission
from math import ceil
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import DebtSerializer, UserSerializer
from rest_framework import permissions

# Create your views here.
#add your gall here

def index(request):
    num_bud = Budget.objects.all().count
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_bud': num_bud,
        'num_visits': num_visits,
    }

    return render(request, 'budget/index.html', context=context)





class BudgetListView(LoginRequiredMixin,  generic.ListView):
    model = Budget
   
    context_object_name = 'budget'
    template_name = 'budget/budget_list.html'

    def get_queryset(self):
         
            return Budget.objects.filter(user=self.request.user).order_by('-income')

        
    def get_context_data(self, **kwargs):
        #call base
       
        context = super().get_context_data(**kwargs)
        #lets use the sessions framework to track views to this page
        #add custom query to pass in
        income = Budget.objects.all().filter(user=self.request.user).aggregate(Sum('income')).pop('income__sum')
        expenses = Budget.objects.all().filter(user=self.request.user).aggregate(Sum('expenses')).pop('expenses__sum')
        context['qs'] = Budget.objects.all().filter(user=self.request.user)
        savings_goal = SavingsGoal.objects.all().filter(user=self.request.user).aggregate(Sum('goal')).pop('goal__sum')
        debt_total = Debt.objects.all().filter(user=self.request.user).aggregate(Sum('amount')).pop('amount__sum')
        if debt_total is not None:
            context['debt_total'] = debt_total
        else:
            context['debt_total'] = 0

        if savings_goal is not None:
            context['savings_goal'] = savings_goal
        else:
            context['savings_goal'] = 0
            
        if income is not None:
            if expenses is not None:
                total = int(income - expenses)
                        
                     
                context["overall_total"] = total
                        

                return context
        
            else:
                context['overall_total'] = 0
                
                return context
class BudgetDetailView(LoginRequiredMixin, generic.DetailView):
    model = Budget
    
    context_object_name = 'budget'
    template_name = 'budget/budget_detail.html'

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        return context
    
    
class BudgetCreateView(LoginRequiredMixin,CreateView):
    model = Budget
    
    fields = ['name', 'income', 'expenses', 'is_monthly', 'is_weekly']
    success_url = reverse_lazy('budget:budget_list')
    template_name = 'budget/budget_create.html'
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(BudgetCreateView, self).form_valid(form)
    
class BudgetUpdateView(LoginRequiredMixin,UpdateView):
    model = Budget
   
    fields = ['name', 'income', 'expenses', 'is_monthly', 'is_weekly']
    template_name = 'budget/budget_create.html'
    success_url = reverse_lazy('budget:budget_list')
    
    def get_queryset(self):
        qs = super(BudgetUpdateView, self).get_queryset()
        return qs.filter(user=self.request.user) 

class BudgetDeleteView(LoginRequiredMixin,DeleteView):
    model = Budget
    
    fields = ['name', 'income', 'expenses', 'is_monthly', 'is_weekly']
    success_url = reverse_lazy('budget:budget_list')

    def get_queryset(self):
        qs = super(BudgetDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)
    
class SearchResultsList(LoginRequiredMixin,generic.ListView):
    model = Budget
    context_object_name = 'budget'
    template_name = 'budget/budget_search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query != '':
            return Budget.objects.filter(user=self.request.user).filter(name__icontains=query)
        
class BusinessCreateView(LoginRequiredMixin,CreateView):
    model = BusinessMessage
    fields = ['email', 'message']
    template_name = 'budget/business_create.html'
    success_url = reverse_lazy('store:home')
#begin savings goal list, detail, crud views

class SavingsGoalListView(LoginRequiredMixin,generic.ListView):
    model = SavingsGoal
  
    context_object_name = 'goals'
    template_name = 'budget/savings-goals/goals_list.html'

    def get_queryset(self):
        return SavingsGoal.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        income = Budget.objects.all().filter(user=self.request.user).aggregate(Sum('income')).pop('income__sum')
        expenses = Budget.objects.all().filter(user=self.request.user).aggregate(Sum('expenses')).pop('expenses__sum')
        current_goal = SavingsGoal.objects.all().filter(user=self.request.user).aggregate(Sum('goal')).pop('goal__sum')
        goals = SavingsGoal.objects.all().filter(user=self.request.user)
        debt_total = Debt.objects.all().filter(user=self.request.user).aggregate(Sum('amount')).pop('amount__sum')
        
        if current_goal is not None:
            context['current_goal'] = current_goal

        if debt_total is not None:
            context['debt_total'] = debt_total
        if goals is not None:
            context['goals'] = goals
        if income is not None:
            if expenses is not None:
                total = int(income-expenses)
                context["net_total"] = total
            else:
                context["net_total"] = 0

       
         
        return context
    
    
class SavingsGoalsDetailView(LoginRequiredMixin,generic.DetailView):
     model = SavingsGoal
     context_object_name = 'goals'
     template_name='budget/savings-goals/goals_detail.html'

     def get_queryset(self):
        return SavingsGoal.objects.filter(user=self.request.user)
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        yearly_goal = SavingsGoal.objects.all().filter(user=self.request.user).aggregate(Sum('goal')).pop('goal__sum')
        if yearly_goal is not None:
            
            context['yearly_goal'] = int(yearly_goal)
            
             
             
          
        return context
#begin crud views for savings goals

class SavingsGoalCreate(LoginRequiredMixin,CreateView):
     model = SavingsGoal
    
     fields = ['name', 'goal', 'deadline']
     success_url = reverse_lazy('budget:savings-goals')
     template_name = 'budget/savings-goals/goals_create.html'

     def form_valid(self, form):
          object = form.save(commit=False)
          object.user = self.request.user
          object.save()
          return super(SavingsGoalCreate, self).form_valid(form)
     
class SavingsGoalUpdate(LoginRequiredMixin,UpdateView):
     model = SavingsGoal
     fields= ['name', 'goal', 'deadline']
     success_url = reverse_lazy('budget:savings-goals')
     template_name  = 'budget/savings-goals/goals_create.html'

     def get_queryset(self):
        qs = super(SavingsGoalUpdate, self).get_queryset()
        return qs.filter(user=self.request.user)
     
class SavingsGoalDelete(LoginRequiredMixin,DeleteView):
     model = SavingsGoal
     fields = ['name', 'goal', 'deadline']
     template_name = 'budget/savings-goals/goals_delete.html'
     success_url = reverse_lazy('budget:savings-goals')

     def get_queryset(self):
        qs = super(SavingsGoalDelete, self).get_queryset()
        return qs.filter(user=self.request.user)
     
#begin debt list and detail views
class DebtListView(LoginRequiredMixin,generic.ListView):
    model = Debt
    context_object_name = 'debt'
    template_name = 'budget/debt/debt_list.html'
    

    def get_queryset(self):
        return Debt.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        savings_goal = SavingsGoal.objects.all().filter(user=self.request.user).aggregate(Sum('goal')).pop('goal__sum')
        income = Budget.objects.all().filter(user=self.request.user).aggregate(Sum('income')).pop('income__sum')
        expenses = Budget.objects.all().filter(user=self.request.user).aggregate(Sum('expenses')).pop('expenses__sum')
        debt_total = Debt.objects.all().filter(user=self.request.user).aggregate(Sum('amount')).pop('amount__sum')

        if income is not None:
            if expenses is not None:
                total = income - expenses
                context['overall_total'] = int(total)

        if debt_total is not None:
            context['debt_total'] = debt_total
        context["qs"] = Debt.objects.all().filter(user=self.request.user)
        context['savings_goal'] = savings_goal
        return context
    
    
class DebtDetailView(LoginRequiredMixin,generic.DetailView):
    model = Debt
    context_object_name = 'debt'
    template_name='budget/debt/debt_detail.html'

    def get_queryset(self):
        return Debt.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = str
        return context
    

class DebtCreate(LoginRequiredMixin,CreateView):
    model = Debt
    fields = ['name', 'amount', 'deadline']
    template_name='budget/debt/debt_create.html'
    success_url = reverse_lazy('budget:debt-list')
    
    def form_valid(self, form):
          object = form.save(commit=False)
          object.user = self.request.user
          object.save()
          return super(DebtCreate, self).form_valid(form)

class DebtUpdate(LoginRequiredMixin,UpdateView):
    model = Debt
    fields = ['name', 'amount', 'deadline']
    template_name='budget/debt/debt_create.html'
    success_url = reverse_lazy('budget:debt-list')

    def get_queryset(self):
        qs = super(DebtUpdate, self).get_queryset()
        return qs.filter(user=self.request.user)
    
class DebtDelete(LoginRequiredMixin,DeleteView):
    model = Debt
    fields = ['name', 'amount', 'deadline']
    template_name='budget/debt/debt_delete.html'
    success_url = reverse_lazy('budget:debt-list')

    def get_queryset(self):
        qs = super(DebtDelete, self).get_queryset()
        return qs.filter(user=self.request.user)

def create_pdf(request):
    #pass in all kinds of shit so people can be ready for tax time.
    #move yearly analytics to down here, dont overload the context datas
    pass
     
    


"""
begin rest api views, this is strictly in dev only
"""
class DebtList(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    

class UserList(generics.ListAPIView):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = UserSerializer
    