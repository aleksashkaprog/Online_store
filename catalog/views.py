from django.shortcuts import render
from django.views import View

from . import services


class CatalogView(services.CatalogProduct, View):
    def get(self, request):
        return render(request, 'catalog.html', {})
