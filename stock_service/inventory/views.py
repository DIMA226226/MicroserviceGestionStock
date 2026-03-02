from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Warehouse, ProductStock
from .serializers import *
from .services import reserve_stock, confirm_stock


class WarehouseListCreate(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductStockListCreate(generics.ListCreateAPIView):
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer


class ReserveStockView(APIView):
    def post(self, request):
        serializer = ReserveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reserve_stock(**serializer.validated_data)
        return Response({"message": "Stock réservé"})


class ConfirmStockView(APIView):
    def post(self, request):
        serializer = ReserveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        confirm_stock(**serializer.validated_data)
        return Response({"message": "Stock confirmé"})