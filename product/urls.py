from django.urls import path
from .views import Product

urlpatterns = [
    path("", Product.as_view(), name="products"),
]
