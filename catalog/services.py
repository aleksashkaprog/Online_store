from django.shortcuts import redirect
from django.views.generic import ListView
from django.urls import reverse

from category.models import Category

from . import utility


class CatalogCategoryService(utility.SearchMixin, utility.CatalogMixin, ListView):

    def get_queryset(self):
        """ Получение продуктов в категории """
        queryset = super().get_queryset()
        category = Category.objects.get(slug=self.kwargs.get('slug'))
        children = category.get_leafnodes()
        return queryset.filter(**({'category__in': children} if children else {'category': category}))

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category_slug'] = self.kwargs.get('slug')
        return context_data


class CatalogCategoryOrderByService(utility.CatalogOrderByMixin, CatalogCategoryService):
    pass


class CatalogProductService(utility.SearchMixin, utility.CatalogMixin, ListView):

    def add_to_compare(self, pk):
        """ Добавление продукта для сравнения """
        products_pk: list = self.session.get('compare', [])
        if pk not in products_pk:
            products_pk.append(pk)
        self.session['compare'] = products_pk
        return redirect(self.META.get('HTTP_REFERER', reverse('compare')))


class CatalogProductOrderByService(utility.CatalogOrderByMixin, CatalogProductService):
    pass


class Discount:

    def check_product_discount(self):
        """ Проверка скидки по продукту """
        pass

    def check_pack_discount(self):
        """ Проверка скидки по набору """
        pass

    def check_cart_discount(self):
        """ Проверка скидки по корзине """
        pass
