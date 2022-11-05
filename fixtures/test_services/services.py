import tempfile

from product.models import Product
from users.models import CustomUser
from category.models import Category
from payment.models import PaymentInfo
from shop.models import Shop, ShopProduct
from order.models import Order, OrderGood


def create_product(name: str = 'test') -> Product:
    """
    Функция, создает товар для тестов
    """
    return Product.objects.create(
        name=name,
        category=Category.objects.create(
            name=name,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
    )


def create_user(email: str = 'test@ya.ru') -> CustomUser:
    """
    Функция, создает пользователя для тестов
    """
    return CustomUser.objects.create_user(email=email, password='test1')


def create_shop(user: CustomUser) -> Shop:
    """
    Функция, создает магазин для тестов
    """
    return Shop.objects.create(name=user.email, slug=user.email, holder=user)


def create_shop_product(shop: Shop, product: Product) -> ShopProduct:
    """
    Функция, создает товар в корзине у пользователя для тестов
    """
    return ShopProduct.objects.create(store=shop, product=product, price=1, old_price=2, amount=1)


def create_order(user: CustomUser) -> Order:
    """ Функция, создает заказ для тестов"""
    return Order.objects.create(consumer=user, first_second_names='Test', phone=99999999, email='test@ya.ru',
                                delivery='обычная', payment='картой', city='Test', address='Test', cost_delivery=1000)


def create_order_good(order: Order, shop_product: ShopProduct) -> OrderGood:
    """ Функция, создает товар в составе заказа для тестов"""
    return OrderGood.objects.create(good=order, seller_good=shop_product,
                                    price_eventual=shop_product.price, quantity=2)


def create_payment_info(order: Order) -> PaymentInfo:
    """ Функция, создает товар в составе заказа для тестов"""
    return PaymentInfo.objects.create(order_id=order.id, cart_number=10203044)
