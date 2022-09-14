from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import Product


class Shop(models.Model):
    """Магазин"""

    name = models.CharField(max_length=512, verbose_name=_("название"))
    holder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shops", verbose_name=_("владелец"))
    address = models.TextField(blank=True, null=True, verbose_name=_("адрес"))
    email = models.EmailField(blank=True, null=True, verbose_name=_("почта"))
    phone = models.CharField(max_length=16, blank=True, null=True, verbose_name=_("телефон"))
    description = models.TextField(blank=True, null=True, verbose_name=_("описание"))
    logo = models.ImageField(upload_to="logo", null=True, verbose_name=_("логотип"))
    slug = models.SlugField(unique=True, verbose_name=_("слаг"))

    def __str__(self):
        return f"Магазин {self.name}"


class ShopProduct(models.Model):
    """Модель продукта магазина"""

    store = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="shop_products", verbose_name=_("магазин")
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="shop_products", verbose_name=_("продукт")
    )
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("цена"))
    amount = models.IntegerField(default=0, verbose_name=_("количество"))
    add_at = models.DateField(auto_now_add=True, verbose_name=_("дата добавления"))

    def __str__(self):
        return f"Продукт {self.product} из магазина {self.store}"
