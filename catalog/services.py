from django.shortcuts import redirect
from django.urls import reverse


class CatalogProduct:

    def add_to_compare(self, pk):
        """ Добавление продукта для сравнения """
        products_pk: list = self.session.get('compare', [])
        if pk not in products_pk:
            products_pk.append(pk)
        self.session['compare'] = products_pk
        return redirect(reverse(self.META.get('HTTP_REFERER', 'catalog')))
