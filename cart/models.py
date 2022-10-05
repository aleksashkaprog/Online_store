from django.contrib.sessions.models import Session
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser
from shop.models import ShopProduct
from product.models import Product


class ProductInCart(models.Model):
    """
    Модель товара, хранящегося в корзине у пользователя
    """

    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='user_carts',
        verbose_name=_('владелец корзины')
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='user_cart_products',
        verbose_name=_('товар')
    )

    shop_product = models.ForeignKey(
        to=ShopProduct,
        on_delete=models.CASCADE,
        related_name='user_cart_shops',
        verbose_name=_('магазин')
    )

    quantity = models.PositiveIntegerField(verbose_name=_('количество'))

    class Meta:
        verbose_name = _('корзина пользователя')
        verbose_name_plural = _('корзины пользователей')

    def __str__(self):
        return f'Товар {self.product.name} в корзине у {self.user.email}'


class ProductInCartAnon(models.Model):
    """
    Модель товара, хранящегося в корзине у анонимного пользователя
    """

    session = models.ForeignKey(
        to=Session,
        on_delete=models.CASCADE,
        related_name='session_carts',
        verbose_name=_('сессия анонимного пользователя')
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='anon_cart_products',
        verbose_name=_('товар')
    )

    shop_product = models.ForeignKey(
        to=ShopProduct,
        on_delete=models.CASCADE,
        related_name='anon_cart_shops',
        verbose_name=_('магазин')
    )

    quantity = models.PositiveIntegerField(verbose_name=_('количество'))

    class Meta:
        verbose_name = _('корзины анонимного пользователя')
        verbose_name_plural = _('корзины анонимных пользователей')

    def __str__(self):
        return f'Товар {self.product.name} в корзине у анонимного пользователя'
