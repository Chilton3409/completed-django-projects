from django.contrib import admin
from .models import Budget, BusinessMessage, SavingsGoal, Debt

# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['name']

class SavingsGoalAdmin(admin.ModelAdmin):
    pass
admin.site.register(SavingsGoal, SavingsGoalAdmin)

class DebtAdmin(admin.ModelAdmin):
    pass

admin.site.register(Debt, DebtAdmin)




admin.site.register(Budget, BudgetAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(BusinessMessage, MessageAdmin)

