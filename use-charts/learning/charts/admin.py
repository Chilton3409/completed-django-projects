from django.contrib import admin
from .models import Bills


# Register your models here.
class BillsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bills, BillsAdmin)
