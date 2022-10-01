from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import Product


class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="banners", verbose_name=_("товар"))
    description = models.CharField(max_length=100, verbose_name=_("описание"))
    logo = models.ImageField(null=True, verbose_name=_("логотип"))
