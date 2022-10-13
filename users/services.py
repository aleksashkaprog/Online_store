from typing import Optional

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

from cart.models import ProductInCart
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


def get_cart_from_anonim(request) -> Optional[dict]:
    """
    Функция, возвращает корзину не авторизованного пользователя
    """
    cart = request.session.get('cart')
    if cart:
        data = {}
        for key, values in cart.items():
            data[key] = {
                'shop_product_id': values['shop_product_id'],
                'quantity': values['quantity'],
                'price': values['price'],
            }

        return data


def move_cart_from_session(cart: dict, user: CustomUser) -> None:
    """
    Функция, преобразует корзину неавторизованного пользователя в корзину авторизованного,
    если у пользователя уже были такие товары в корзине, суммирует количество
    """
    for product_id, data in cart.items():
        try:
            product = ProductInCart.objects.get(user=user, shop_product__product__id=product_id)

            if product.shop_product.id == data['shop_product_id']:
                product.quantity += data['quantity']
                product.save()
            else:
                product.delete()
                raise ProductInCart.DoesNotExist

        except ProductInCart.DoesNotExist:
            ProductInCart.objects.create(
                user=user,
                shop_product_id=data['shop_product_id'],
                quantity=data['quantity']
            )
