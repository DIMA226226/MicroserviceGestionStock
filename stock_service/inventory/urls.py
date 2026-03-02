"""from django.urls import path
from .views import *
from .views import WarehouseListCreate  

urlpatterns = [
    path('warehouses/', WarehouseListCreate.as_view()),
    path('stocks/', ProductStockListCreate.as_view()),
    path('stocks/reserve/', ReserveStockView.as_view()),
    path('stocks/confirm/', ConfirmStockView.as_view()),
]"""

from django.urls import path
from .views import WarehouseListCreate, ProductStockListCreate, ReserveStockView, ConfirmStockView

urlpatterns = [
    path('warehouses/', WarehouseListCreate.as_view(), name='warehouse-list'),
    path('product-stocks/', ProductStockListCreate.as_view(), name='productstock-list'),
    path('reserve-stock/', ReserveStockView.as_view(), name='reserve-stock'),
    path('confirm-stock/', ConfirmStockView.as_view(), name='confirm-stock'),
]