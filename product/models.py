from django.db import models
from django.utils.translation import gettext_lazy as _

from category.models import Category
from category.tools import get_slug


class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=512, unique=True, verbose_name=_('название'))
    slug = models.SlugField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('цена'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    views = models.PositiveIntegerField(default=0, verbose_name=_('просмотры'))
    images = models.ManyToManyField('Image', verbose_name=_('изображения'))
    # comments = models.ManyToManyField('Comment', verbose_name=_('комментарии'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('дата обновления'))
    description = models.TextField(verbose_name=_('описание'))

    def save(self, *args, **kwargs) -> 'Product':
        self.slug = get_slug(self.name)
        return super().save(*args, **kwargs)


class Image(models.Model):
    """Модель изображений товара"""
    pass
