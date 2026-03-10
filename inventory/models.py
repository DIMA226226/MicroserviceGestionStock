import uuid
from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductStock(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4)
    variant_id = models.UUIDField(null=True, blank=True)

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    quantity_available = models.IntegerField(default=0)
    quantity_reserved = models.IntegerField(default=0)

    minimum_threshold = models.IntegerField(default=5)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ('product_id', 'variant_id', 'warehouse')


class StockMovement(models.Model):

    MOVEMENT_TYPES = [
        ('IN', 'Entrée'),
        ('OUT', 'Sortie'),
        ('RETURN', 'Retour'),
        ('RESERVE', 'Réservation'),
        ('RELEASE', 'Annulation'),
        ('ADJUSTMENT', 'Ajustement'),
        ('TRANSFER', 'Transfert'),
    ]

    product_id = models.UUIDField()
    variant_id = models.UUIDField(null=True, blank=True)

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField()
    reference = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)