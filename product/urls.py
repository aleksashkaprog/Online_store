from django.urls import path
from .views import ProductDetail

urlpatterns = [
    path("<int:pk>/", ProductDetail.as_view(), name="product"),
]
