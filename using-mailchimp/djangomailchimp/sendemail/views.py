from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.conf import settings
from .forms import EmailForm


# Create your views here.
def subscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            return redirect('subscribe-success')
        
    return render(request, 'subscribe.html', {
        'form': EmailForm(),
    })


def subscribe_success_view(request):
    return render(request, 'message.html', {
        'title': 'Successfully subscribed',
        'message': 'You have successfully subscribed to our mailing list'

    })

def subscribe_fail_view(request):
    return render(request, 'message.html', {
        'title': 'Failed to subscribe, please try again',
        'message':'Oops, something went wrong'})

def unsubscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            #todo, use mailchimp api to unsubscribe
            return redirect('unsubscribe-success')
    return render(request, 'unsubscribe.html', {
        'form': EmailForm(),

    })

def unsubscribe_success_view(request):
    return render(request, 'message.html', {
        'title': 'Successfully Unsubscribed!',
        'message': 'You have unsubscribed from our mailing list',
    })
def unsubscribe_fail_view(request):
    return render(request, 'message.html', {
        'title': 'Something went wrong, contact an admin for support.',
        'message': 'Oops, something went wrong',

    })
        
    
