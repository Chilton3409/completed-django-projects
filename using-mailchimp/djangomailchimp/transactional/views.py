from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def send_view(request):
    return JsonResponse({
        'detail': 'This view is going to send email',

    })

