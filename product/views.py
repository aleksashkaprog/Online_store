# from django.shortcuts import render
from django.db.models import QuerySet
from django.http import HttpResponse

from . import models


def product_view(request) -> HttpResponse:
    products: QuerySet = models.Product.objects.all()
    return HttpResponse(products)
