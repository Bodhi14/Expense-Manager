from django.contrib import admin
from .models import Expense

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'amount',)

admin.site.register(Expense, ExpenseAdmin)
