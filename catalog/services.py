from django.shortcuts import redirect
from django.urls import reverse


class Catalog:

    def get_products(self):
        """ Получение продуктов в категории """
        pass

    def get_product(self):
        """ Получение конкретного продукта"""
        pass

    def get_shop_info(self):
        """ Получение информации о продавце """
        pass

    def get_discounts(self):
        """ Получение информации о скидках """
        pass


class CatalogProduct:

    def add_review(self):
        """ Добавление отзыва к продукту """
        pass

    def add_to_compare(self, pk):
        """ Добавление продукта для сравнения """
        products_pk: list = self.session.get('compare', [])
        if pk not in products_pk:
            products_pk.append(pk)
        self.session['compare'] = products_pk
        return redirect(reverse(self.META.get('HTTP_REFERER', 'catalog')))


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
