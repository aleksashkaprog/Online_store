from .models import PackDiscount
from django.utils.translation import gettext_lazy as _
from product.models import Product

class PackDiscountServices:

    @staticmethod
    def valid_discount(obj: PackDiscount) -> str:
        if (obj.products.filter(pack_discounts__group=1).exists() or
            obj.categories.filter(pack_discounts__group=1).exists()) and \
                (obj.products.filter(pack_discounts__group=2).exists() or
                 obj.categories.filter(pack_discounts__group=2).exists()):
            return _('Да')
        else:
            return _('Нет, добавьте обе группы товаров')


class DiscountServices:

    @staticmethod
    def get_all_discounts(*products: Product):
        discount_list = []
        for product in products:
            discounts = product.discounts.all()
            print(discounts)
            discount_list.append(discounts)
