from django.urls import path
from .views import Shop, CreateShop, CreateGood, EditShop, EditGood

urlpatterns = [
    path("", Shop.as_view(), name="shop"),
    path("create/shop/", CreateShop.as_view(), name="create-shop"),
    path("create/good/", CreateGood.as_view(), name="create-good"),
    path("edit/shop/", EditShop.as_view(), name="edit-shop"),
    path("edit/good/", EditGood.as_view(), name="edit-good"),
]
