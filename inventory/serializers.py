from rest_framework import serializers
from .models import Warehouse, ProductStock


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class ProductStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStock
        fields = '__all__'


class ReserveSerializer(serializers.Serializer):
    product_id = serializers.UUIDField()
    warehouse_id = serializers.IntegerField()
    quantity = serializers.IntegerField()