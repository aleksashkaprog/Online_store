import random
from decimal import Decimal

from django.http import Http404
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404

from product.models import Product
from shop.models import ShopProduct
from cart.forms import CartAddProductForm
from cart.models import ProductInCart, ProductInCartAnon


class Cart(object):
    """Класс, описывающий корзину пользователя"""

    def __init__(self, request) -> None:
        """Инициализируем корзину"""
        self.auth = request.user.is_authenticated

        if not self.auth:
            if not request.session.session_key:
                request.session.create()

            self.session = Session.objects.only('pk').get(session_key=request.session.session_key)
            self.cart = self.session.session_carts.all().prefetch_related(
                'product__shop_products__store', 'product__images')

        else:
            self.user = request.user
            self.cart = self.user.user_carts.all().prefetch_related(
                'product__shop_products__store', 'product__images')

    def add(self, product: Product, shop_product: ShopProduct, quantity: int = 1,
            update_quantity: bool = False) -> None:
        """Добавить продукт в корзину или обновить его количество"""
        try:
            if self.auth:
                cart_product_model = ProductInCart(user=self.user)
                cart_product = ProductInCart.objects.only(
                    'shop_product', 'quantity').get(user=self.user, product_id=product.id)

            else:
                cart_product_model = ProductInCartAnon(session_id=self.session.pk)
                cart_product = ProductInCartAnon.objects.only(
                    'shop_product', 'quantity').get(session_id=self.session.pk, product_id=product.id)

            if cart_product.shop_product_id != shop_product.id:
                cart_product.shop_product_id = shop_product.id
                update_quantity = True

            if update_quantity:
                cart_product.quantity = quantity
            else:
                cart_product.quantity += quantity

            cart_product.save(update_fields=['shop_product', 'quantity'])

        except cart_product_model.DoesNotExist:
            cart_product_model.product_id = product.id
            cart_product_model.shop_product_id = shop_product.id
            cart_product_model.quantity = quantity

            cart_product_model.save()

    def remove(self, product: Product) -> None:
        """Удаление товара из корзины"""
        if self.auth:
            cart_product = get_object_or_404(klass=ProductInCart, user=self.user, product_id=product.id)
        else:
            cart_product = get_object_or_404(klass=ProductInCartAnon, session_id=self.session.pk, product_id=product.id)

        cart_product.delete()

    def __iter__(self) -> dict:
        """Перебор элементов в корзине"""
        for item in self.cart:
            yield item

    def __len__(self) -> int:
        """Подсчет всех товаров в корзине"""
        return sum([item.quantity for item in self.cart])

    def get_total_price(self) -> int:
        """Подсчет стоимости товаров в корзине"""
        return sum([Decimal(item.shop_product.price * item.quantity) for item in self.cart])

    def clear(self) -> None:
        """Удаление корзины из БД"""
        for cart_product in self.cart:
            cart_product.delete()


def get_product(pk: int, *args) -> Product:
    """Возвращает продукт"""
    try:
        return Product.objects.only(*args).get(id=pk)
    except ShopProduct.DoesNotExist:
        raise Http404


def get_shop_product(pk: int) -> ShopProduct:
    """Возвращает магазин"""
    try:
        return ShopProduct.objects.only('id').get(id=pk)
    except ShopProduct.DoesNotExist:
        raise Http404


def get_random_shop_product(product_id: int) -> ShopProduct:
    return random.choice(ShopProduct.objects.only('id').all().filter(product_id=product_id))


def get_data_for_add_to_cart(request, product_pk: int, shop_product_pk: int) -> tuple:
    """Возвращает данные для представления добавления товара в корзину"""
    product = get_product(product_pk, 'id')
    shop_product = get_shop_product(shop_product_pk) if shop_product_pk else get_random_shop_product(product_pk)

    if request.method == 'GET':
        form = None
    else:
        form = CartAddProductForm(request.POST)

    return shop_product, product, form


def add_product_to_cart(request, form, product: Product, shop_product: ShopProduct) -> None:
    """Добавляет товар в корзину"""
    cart = Cart(request)

    data_for_add = {
        'product': product,
        'shop_product': shop_product,
    }

    if form:
        data = form.cleaned_data
        data_for_add['quantity'] = data['quantity']
        data_for_add['update_quantity'] = data['update']

    cart.add(**data_for_add)


def remove_product(request, pk: int) -> None:
    """Удаляет товар из корзины"""
    cart = Cart(request)
    product = get_product(pk, 'id')
    cart.remove(product)
