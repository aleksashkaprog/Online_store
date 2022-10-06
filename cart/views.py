from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .services import add_product_to_cart, get_data_for_add_to_cart, remove_product


class CartView(TemplateView):
    """Представление корзины пользователя"""
    template_name = 'cart.html'


def cart_add(request, product_pk, shop_product_pk=None):
    """Добавляет товар в корзину"""
    shop_product, product, form = get_data_for_add_to_cart(request, product_pk, shop_product_pk)

    if request.method == 'POST' and form.is_valid():
        add_product_to_cart(request, form, product, shop_product)

    return redirect(reverse(viewname='product', kwargs={'slug': product.slug, 'pk': product.id}))


def cart_remove(request, pk: int):
    """Удаляет товар из корзины"""
    remove_product(request, pk)
    return redirect('cart:cart')
