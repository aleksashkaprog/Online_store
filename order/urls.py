from django.urls import path
from .views import OrderHistory, Order

urlpatterns = [
    path('', OrderHistory.as_view(), name='history-order'),
    path('oneorder/', Order.as_view(), name='one-order')
]
