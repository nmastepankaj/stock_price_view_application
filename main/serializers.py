from rest_framework import serializers
from .models import Stock, Company

class CompanySerializer(serializers.ModelSerializer):
    """Serializer for Company Model"""
    class Meta:
        model = Company
        fields = ['id', 'name']

class StockSerializer(serializers.ModelSerializer):
    """Serializer for Stock Model"""
    company = CompanySerializer()
    class Meta:
        model = Stock
        fields = ['id', 'company', 'date', 'open', 'close', 'high', 'low', 'last', 'prev_close', 'no_trades', 'no_of_shrs', 'net_turnover']

class FavouriStockSerializer(serializers.ModelSerializer):
    """Serializer for Favourite Stock Model"""
    stock = CompanySerializer()
    class Meta:
        model = Stock
        fields = ['id', 'stock']