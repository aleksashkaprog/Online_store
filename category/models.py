from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

from . import utility
from . import tools


class Category(utility.StrMixin, MPTTModel):
    """Категории продуктов"""
    name = models.CharField(max_length=128, unique=True, verbose_name=_('наименование'))
    slug = models.SlugField(max_length=256, blank=True, verbose_name=_('slug'))
    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name=_('родитель'))
    image = models.FileField(upload_to=tools.get_path, null=True, blank=True, verbose_name=_('иконка'))

    def save(self, *args, **kwargs):
        self.slug = tools.get_slug(self.name)
        return super().save(*args, **kwargs)
