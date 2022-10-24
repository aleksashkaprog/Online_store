from .models import PackDiscount
from django.utils.translation import gettext_lazy as _


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
