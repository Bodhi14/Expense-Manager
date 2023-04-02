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
from rest_framework import status

from app import serializers

class ExpenseAPI(APIView):

    permission_classes = [ AllowAny ]

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            expenseitem = Expense.objects.get(pk=id)
            serializer = ExpenseSerializer(expenseitem)
            return Response(serializer.data)
        qs = Expense.objects.all()
        serializer = ExpenseSerializer(qs, many=True)
        return Response(serializer.data)


    def post(self, request, pk=None, format=None):
        serializer = ExpenseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            qs = Expense.objects.all()
            alldataserializer = ExpenseSerializer(qs, many=True)

            return Response({'msg': 'New Expense added', 'data-added': serializer.data, 'data': alldataserializer.data}, status=status.HTTP_201_CREATED)
        return Response(alldataserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            Expense.objects.get(pk=id).delete()
            expenses = Expense.objects.all()
            serializer = ExpenseSerializer(expenses, many=True)
            return Response({'msg': 'Expense with id   ' + str(id) + 'is deleted', 'data': serializer.data})


        qs = Expense.objects.all()
        if qs:
            qs.last().delete()
            serializer = ExpenseSerializer(qs, many=True)
            return Response({'msg': 'Last Expense Deleted', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            expense = Expense.objects.get(pk=id)
            serializer = ExpenseSerializer(expense, data=request.data)

            if serializer.is_valid():
                serializer.save()
                qs = Expense.objects.all()
                alldataserializer = ExpenseSerializer(qs, many=True)
                return Response({'msg' : 'Expense having ID : ' + str(id) + ' is updated', 'data-updated': serializer.data,'data': serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'Cannot update the expense' + str(id), 'data': serializer.data})

    def patch(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            expense = Expense.objects.get(pk=id)
            serializer = ExpenseSerializer(expense, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                qs = Expense.objects.all()
                alldataserializer = ExpenseSerializer(qs, many=True)
                return Response({'msg' : 'Expense having ID : ' + str(id) + ' is updated', 'data-updated': serializer.data ,'data': alldataserializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'Cannot update the expense' + str(id), 'data': serializer.data})











# @api_view(['GET', 'POST', 'DELETE', 'PUT'])
# @permission_classes([AllowAny])
# def expense_list(request):
#     if request.method == 'GET':
#         qs = Expense.objects.all()
#         serializer = ExpenseSerializer(qs, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ExpenseSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     if request.method == 'DELETE':
#         qs = Expense.objects.all()
#         if qs:
#             qs.last().delete()
#             serializer = ExpenseSerializer(qs, many=True)
#             return Response(serializer.data)
#         return Response(serializer.errors)

# @api_view(['GET', 'POST', 'DELETE', 'PUT'])
# @permission_classes([AllowAny])
# def expense_detail(request, pk):
#     if request.method == 'GET':
#         expense = Expense.objects.get(pk=pk)
#         if expense:
#             serializer = ExpenseSerializer(expense)
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     if request.method == 'DELETE':
#         to_delete = Expense.objects.get(pk=pk)
#         if to_delete:
#             to_delete.delete()
#             qs = Expense.objects.all()
#             serializer = ExpenseSerializer(qs, many=True)
#             return Response({'msg': 'Expense deleted'})
#         return Response(serializer.errors)
















# Create your views here.
