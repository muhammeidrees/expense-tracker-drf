from rest_framework import serializers
from .models import Transactions,Category

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"