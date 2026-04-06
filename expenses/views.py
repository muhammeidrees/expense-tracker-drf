from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Category,Transactions
from django.db.models import Sum
from .serializers import CategorySerializer,TransactionsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer
    
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset= Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Transactions.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

@api_view(["GET"])
def get_balance(request):
    transactions = Transactions.objects.filter(user=request.user)
    income = sum(t.amount for t in transactions if t.type == "INCOME")       
    expense = sum(t.amount for t in transactions if t.type == "EXPENSE")       
    balance = income - expense
    
    return Response({
        "income":income,
        "expense":expense,
        "balance":balance
    })
    
@api_view(["GET"])
def monthly_report(request):
    data = Transactions.objects.filter(user=request.user).values("category__name").annotate(total = Sum("amount"))
    return Response(data)

