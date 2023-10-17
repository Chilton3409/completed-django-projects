from django.shortcuts import render
from django.views.generic import TemplateView
from allauth.account.views import LoginView, SignupView, PasswordChangeView, PasswordResetView, LogoutView


# Create your views here.

def home(request):
    context = {}
    return render(request, 'social_app/home.html', context=context)

#overwrite views for 3rd party login to make desing much fresher and then take the templates from the allauth dir

class MyLoginView(LoginView):
    template_name = 'account/login.html'

class MySignUpView(SignupView):
    template_name = 'account/signup.html'


class MyChangePasswordView(PasswordChangeView):
    template_name = 'account/change_password.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'

class MyLogoutView(LogoutView):
    template_name = 'account/logout.html'

