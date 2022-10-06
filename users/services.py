from typing import List, Optional

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

from cart.models import ProductInCart
from cart.services import Cart
from users.models import CustomUser


def register_user(request, user_form) -> None:
    """
    Функция, создает пользователя и авторизует его
    """
    user_form.save()

    anonim_cart = get_cart_from_anonim(request)
    email = user_form.cleaned_data.get('email')
    raw_password = user_form.cleaned_data.get('password1')

    user = authenticate(email=email, password=raw_password)

    if anonim_cart and user:
        move_cart_from_session(anonim_cart, user)

    group = Group.objects.get(name='customer')
    user.groups.add(group)

    login(request, user)


def login_user(request, form) -> CustomUser:
    """
    Функция, авторизует пользователя
    """
    anonim_cart = get_cart_from_anonim(request)
    user = form.cleaned_data
    login(request, user)

    if anonim_cart and user:
        move_cart_from_session(anonim_cart, user)

    return user


def password_change(request, user_form) -> None:
    """
    Функция заглушка для представления восстановления пароля
    """
    email = user_form.cleaned_data.get('email')
    user = CustomUser.objects.get(email=email)
    user.set_password('qwerty1234')
    user.save()


def get_cart_from_anonim(request) -> Optional[List[dict]]:
    """
    Функция, возвращает корзину не авторизованного пользователя
    """
    cart = Cart(request)

    if cart:
        cart_list = []
        for product_cart in cart:
            data = {
                'product': product_cart.product,
                'quantity': product_cart.quantity,
                'shop_product': product_cart.shop_product
            }
            cart_list.append(data)

        return cart_list


def move_cart_from_session(cart: list, user: CustomUser) -> None:
    """
    Функция, преобразует корзину неавторизованного пользователя в корзину авторизованного,
    если у пользователя уже были такие товары в корзине, суммирует количество
    """
    if cart is not None and cart:
        for product_cart in cart:

            try:
                product = ProductInCart.objects.get(product=product_cart['product'], user=user)

                if product.shop_product == product_cart['shop_product']:
                    product.quantity += product_cart['quantity']
                    product.save()
                else:
                    product.delete()
                    raise ProductInCart.DoesNotExist

            except ProductInCart.DoesNotExist:
                ProductInCart.objects.create(
                    user=user,
                    product=product_cart['product'],
                    shop_product=product_cart['shop_product'],
                    quantity=product_cart['quantity']
                )
