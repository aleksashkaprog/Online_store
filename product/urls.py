from django.urls import path
from .views import ProductDetail


urlpatterns = [
    path("<str:slug>/", ProductDetail.as_view(), name='product'),
]
