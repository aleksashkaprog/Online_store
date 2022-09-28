from django.shortcuts import render
from django.views import View

from product.models import Product

from . import services


class CompareView(services.CompareServices, View):
    def get(self, request):
        products = Product.objects.filter(pk__in=request.session.get('compare', []))
        context = dict(products=products)
        return render(request, 'compare/compare.html', context)
