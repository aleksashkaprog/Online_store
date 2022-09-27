from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

from category.models import Category
from category.tools import get_slug


class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=512, unique=True, verbose_name=_('название'))
    slug = models.SlugField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('цена'))
    old_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('старая цена'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    views = models.PositiveIntegerField(default=0, verbose_name=_('просмотры'))
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5), ], verbose_name=_('рейтинг'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('дата обновления'))
    description = models.TextField(verbose_name=_('описание'))
    characteristic = models.TextField(verbose_name=_('характеристика'))

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> 'Product':
        self.slug: str = get_slug(self.name)
        return super().save(*args, **kwargs)

    def get_characteristic(self) -> dict:
        dict_characteristic: dict = {i.split(' - ')[0]: i.split(' - ')[1] for i in self.characteristic.split(', ')}
        return dict_characteristic
