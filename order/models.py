from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from shop.models import ShopProduct

DELIVERY_CHOICES = [("обычная", _("Обычная доставка")), ("экспресс", _("Экспресс доставка"))]

PAYMENT_CHOICES = [("картой", _("Картой")), ("наличными", _("Наличными"))]


class Order(models.Model):
    consumer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="orders", verbose_name=_("потребитель")
    )
    first_second_names = models.TextField(null=True, blank=True, verbose_name=_("ФИО"))
    phone = models.CharField(max_length=13, verbose_name=_("телефон"))
    email = models.EmailField(verbose_name=_("почта"))
    delivery = models.CharField(max_length=10, default="обычная", choices=DELIVERY_CHOICES, verbose_name=_("доставка"))
    payment = models.CharField(max_length=10, default="картой", choices=PAYMENT_CHOICES, verbose_name=_("оплата"))
    city = models.CharField(max_length=30, verbose_name=_("город"))
    address = models.CharField(max_length=50, verbose_name=_("адрес"))
    paid = models.BooleanField(default=False, verbose_name=_("оплачен заказ"))
    cost_delivery = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name=_("стоимость доставки")
    )
    order_in = models.BooleanField(default=False, verbose_name=_("в заказе"))
    ordered = models.DateTimeField(null=True, blank=True, verbose_name=_("время заказа"))

    def __str__(self):
        return f"Order №{self.id}"

    def __len__(self):
        return len(self.order_goods.all())

    @property
    def all_goods_price(self):
        sum = 0
        for good in self.order_goods.all():
            sum += good.quantity * good.seller_good.price
        return sum

    @property
    def all_goods_price_disc_delivery(self):
        sum = 0
        for good in self.order_goods.all():
            sum += good.quantity * good.price_eventual
        return sum + self.cost_delivery

    class Meta:
        verbose_name = _("заказ")
        verbose_name_plural = _("заказы")


class OrderGood(models.Model):
    good = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_goods", verbose_name=_("продукт в заказе")
    )
    seller_good = models.ForeignKey(
        ShopProduct, on_delete=models.CASCADE, related_name="order_goods", verbose_name=_("продавец")
    )
    price_eventual = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("цена"))
    quantity = models.IntegerField(default=1, verbose_name=_("количество"))

    def __str__(self):
        return f"Продукт в заказе №{self.id}"

    class Meta:
        verbose_name = _("продуктв в заказе")
        verbose_name_plural = _("продукты в заказе")
