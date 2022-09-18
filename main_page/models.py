from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import Product


class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="banners", verbose_name=_("товар"))
    logo = models.ImageField(upload_to="logo", null=True, verbose_name=_("логотип"))
