# from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class Shop(TemplateView):
    template_name = "inc/shop/seller_home.html"


class CreateShop(TemplateView):
    template_name = "inc/shop/create_shop.html"


class CreateGood(TemplateView):
    template_name = "inc/shop/create_good.html"


class EditShop(TemplateView):
    template_name = "inc/shop/edit_shop.html"


class EditGood(TemplateView):
    template_name = "inc/shop/edit_good.html"
