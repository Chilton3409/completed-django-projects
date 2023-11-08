from typing import List
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CustomUser

from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UserListView(LoginRequiredMixin, generic.ListView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['email']
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:my-profile')

    def get_queryset(self):
        qs = super(UserUpdateView, self).get_queryset()
        return qs.filter(email=self.request.user) 

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    fields = ['email']
    success_url = reverse_lazy('store:home')

    def get_queryset(self):
        qs = super(UserDeleteView, self).get_queryset()
        return qs.filter(email=self.request.user)

