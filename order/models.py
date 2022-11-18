from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from cart.models import ProductInCart

DELIVERY_CHOICES = [("обычная", _("Обычная доставка")), ("экспресс", _("Экспресс доставка"))]

PAYMENT_CHOICES = [("картой", _("Картой")), ("наличными", _("Наличными"))]


class Order(models.Model):
    consumer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="orders", verbose_name=_("потребитель")
    )
    first_second_names = models.TextField(null=True, blank=True, verbose_name=_("ФИО"))
    phone = models.CharField(null=True, blank=True, max_length=13, verbose_name=_("телефон"))
    email = models.EmailField(null=True, blank=True, verbose_name=_("почта"))
    delivery = models.CharField(max_length=10, default="обычная", choices=DELIVERY_CHOICES, verbose_name=_("доставка"))
    payment = models.CharField(max_length=10, default="картой", choices=PAYMENT_CHOICES, verbose_name=_("оплата"))
    city = models.CharField(null=True, blank=True, max_length=30, verbose_name=_("город"))
    address = models.CharField(null=True, blank=True, max_length=50, verbose_name=_("адрес"))
    paid = models.BooleanField(default=False, verbose_name=_("оплачен заказ"))
    cost_delivery = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name=_("стоимость доставки")
    )
    order_in = models.BooleanField(default=False, verbose_name=_("в заказе"))
    ordered = models.DateTimeField(null=True, blank=True, verbose_name=_("время заказа"))

    def __str__(self):
        return f"Заказ №{self.id}"

    def __len__(self):
        return len(self.order_goods.all())

    def get_absolute_url(self):
        return reverse("one-order", args=[str(self.id)])

    @property
    def all_goods_price(self):
        sum = 0
        for good in self.order_goods.all():
            sum += good.good_in_cart.shop_product.amount * good.good_in_cart.shop_product.old_price
        return sum

    @property
    def all_goods_price_disc_delivery(self):
        sum = 0
        for good in self.order_goods.all():
            sum += good.good_in_cart.shop_product.amount * good.good_in_cart.shop_product.price
        return sum + self.cost_delivery

    class Meta:
        ordering = ["-ordered"]
        verbose_name = _("заказ")
        verbose_name_plural = _("заказы")


class OrderGood(models.Model):
    good_in_order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_goods", verbose_name=_("продукт в заказе")
    )
    good_in_cart = models.ForeignKey(
        ProductInCart,
        default=None,
        on_delete=models.CASCADE,
        related_name="order_goods",
        verbose_name=_("продукт в корзине"),
    )

    def __str__(self):
        return f"Продукт в заказе №{self.id}"

    class Meta:
        verbose_name = _("продукт в заказе")
        verbose_name_plural = _("продукты в заказе")
