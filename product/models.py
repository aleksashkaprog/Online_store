from django.db import models
from django.utils.translation import gettext_lazy as _

from django.core.validators import MaxValueValidator, MinValueValidator
import os

from category.models import Category
from category.tools import get_slug


def load_images(instance, filename):
    path = "product_images/"
    file_name = f'{instance.product.slug}_{instance.product.id}.{filename.split(".")[-1]}'
    return os.path.join(path, file_name)


class Product(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=512, unique=True, verbose_name=_('название'))
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
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


class Image(models.Model):
    file = models.ImageField(upload_to=load_images, verbose_name=_('файл'))
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='images', verbose_name=_('продукт'))

    def __str__(self):
        return f'{self.file.url}'


class Review(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='reviews', verbose_name=_('товар'))
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             related_name='reviews', verbose_name=_('пользователь'))
    text = models.CharField(max_length=1000, verbose_name=_('текст отзыва'))
    rating = models.SmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(5)),
                                      verbose_name=_('Оценка'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'))

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.full_name}: {self.rating}'
