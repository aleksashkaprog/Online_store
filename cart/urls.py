from django.urls import path
from .views import cart_add, CartView, cart_remove


app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:product_pk>/', cart_add, name='cart_random_add'),
    path('add/<int:product_pk>/<int:shop_product_pk>/', cart_add, name='cart_add'),
    path('remove/<int:pk>/', cart_remove, name='cart_remove'),
]
