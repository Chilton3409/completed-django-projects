from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Bills

# Create your views here.

class BillsChartView(TemplateView):
    template_name = 'charts/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Bills.objects.all()
        return context
    