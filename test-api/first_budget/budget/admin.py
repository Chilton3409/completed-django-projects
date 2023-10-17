from django.contrib import admin
from . models import *

# Register your models here.
class IncomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Income, IncomeAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Expense, ExpenseAdmin)

class BudgetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Budget, BudgetAdmin)