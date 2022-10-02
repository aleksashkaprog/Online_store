import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import ShopProduct
from users.models import CustomUser


class Favourite(models.Model):
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, related_name='favourites', verbose_name=_('продукт'))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favourites', verbose_name=_('пользователь'))


class DayOffer(models.Model):
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, related_name='dayoffers', verbose_name=_('продукт'))
    day = models.DateField(default=datetime.date.today(), verbose_name=_('день'))


class Top(models.Model):
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, related_name='top_products', verbose_name=_('продукт'))


class Hot(models.Model):
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, related_name='hots', verbose_name=_('продукт'))


class Limit(models.Model):
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, related_name='limits', verbose_name=_('продукт'))