import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


def update_avatar(instance, filename):
    path = "avatars/"
    file_name = f'{instance.user.email}_avatar.{filename.split(".")[-1]}'
    return os.path.join(path, file_name)


class CustomUser(AbstractUser):
    """
    Модель кастомного пользователя
    """
    username = None
    email = models.EmailField(verbose_name=_('e-mail'), max_length=128, unique=True)
    phone_number = models.CharField(verbose_name=_('телефон'), max_length=12, blank=True)
    full_name = models.CharField(verbose_name=_('ФИО'), max_length=256, blank=True)
    avatar = models.ImageField(verbose_name=_('аватар'), upload_to=update_avatar)

    is_staff = models.BooleanField(verbose_name=_('работник'), default=False)
    is_active = models.BooleanField(verbose_name=_('флаг активности'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')

        permissions = (
            ('can_do_order', _('Может делать заказ')),
        )

    def __str__(self):
        return self.email
