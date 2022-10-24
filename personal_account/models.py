from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.models import ShopProduct
from users.models import CustomUser


class ViewsHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('пользователь'))
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE, verbose_name=_('продукт'))
