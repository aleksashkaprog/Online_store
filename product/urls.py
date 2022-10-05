from django.urls import path
from .views import ProductDetail

urlpatterns = [
    path("<slug:slug>/<int:pk>/", ProductDetail.as_view(), name='product'),
]
