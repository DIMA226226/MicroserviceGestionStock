from django.db import transaction
from django.db.models import F
from rest_framework.exceptions import ValidationError
from .models import ProductStock, StockMovement


def reserve_stock(product_id, warehouse_id, quantity):

    with transaction.atomic():

        stock = ProductStock.objects.select_for_update().get(
            product_id=product_id,
            warehouse_id=warehouse_id
        )

        real_available = stock.quantity_available - stock.quantity_reserved

        if real_available < quantity:
            raise ValidationError("Stock insuffisant")

        stock.quantity_reserved = F('quantity_reserved') + quantity
        stock.save()

        StockMovement.objects.create(
            product_id=product_id,
            warehouse_id=warehouse_id,
            movement_type='RESERVE',
            quantity=quantity
        )


def confirm_stock(product_id, warehouse_id, quantity):

    with transaction.atomic():

        stock = ProductStock.objects.select_for_update().get(
            product_id=product_id,
            warehouse_id=warehouse_id
        )

        stock.quantity_reserved -= quantity
        stock.quantity_available -= quantity
        stock.save()

        StockMovement.objects.create(
            product_id=product_id,
            warehouse_id=warehouse_id,
            movement_type='OUT',
            quantity=quantity
        )