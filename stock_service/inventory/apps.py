"""
from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'

    def ready(self):
        # Importe et initialise Eureka au démarrage de Django
        import stock_service.eureka

"""

from django.apps import AppConfig

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'

    def ready(self):
        import stock_service.eureka  # Ceci importe et lance l'inscription Eureka
