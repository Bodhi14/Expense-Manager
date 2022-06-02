
from tkinter.tix import STATUS
from django.shortcuts import render
from django.urls import path 
from . import views

from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib import admin
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *
from rest_framework.response import Response
from .serializers import ExpenseSerializer
from app.models import Expense

from app import serializers

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def expense_list(request):
    if request.method == 'GET':
        qs = Expense.objects.all()
        serializer = ExpenseSerializer(qs, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ExpenseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        qs = Expense.objects.all()
        if qs:
            qs.last().delete()
            serializer = ExpenseSerializer(qs, many=True)
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def expense_detail(request, pk):
    if request.method == 'GET':
        expense = Expense.objects.get(pk=pk)
        if expense:
            serializer = ExpenseSerializer(expense)
            return Response(serializer.data)
        return Response(serializer.errors)
        
    if request.method == 'DELETE':
        to_delete = Expense.objects.get(pk=pk)
        if to_delete:
            to_delete.delete()
            qs = Expense.objects.all()
            serializer = ExpenseSerializer(qs, many=True)
            return Response({'msg': 'Expense deleted'})
        return Response(serializer.errors)

    
    

    


    


        
        




# Create your views here.
