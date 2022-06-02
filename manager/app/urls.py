
import imp
from django.urls import path
from . import views
from .views import expense_list, expense_detail

urlpatterns = [
    path('expenses-api/', expense_list),
    path('expense-detail-api/<int:pk>/', expense_detail)
    
]
