import tempfile

from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from product.models import Product
from category.models import Category
from shop.models import Shop, ShopProduct
from users.models import CustomUser
from cart.models import ProductInCart, ProductInCartAnon


def create_product() -> Product:
    """
    Функция, создает товар для тестов
    """
    return Product.objects.create(
        name='test',
        category=Category.objects.create(
            name='test',
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
    return Shop.objects.create(name='test', slug=user.email, holder=user)


def create_shop_product(shop: Shop, product: Product) -> ShopProduct:
    """
    Функция, создает товар в корзине у пользователя для тестов
    """
    return ShopProduct.objects.create(store=shop, product=product, price=1, old_price=2, amount=1)


class CartDetailViewTest(TestCase):
    def setUp(self):
        self.get_response = self.client.get(reverse(viewname='cart:cart'))

    def test_view_url_exist_at_desired_location(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.assertEqual(self.get_response.status_code, 200)

    def test_view_use_correct_template(self):
        self.assertEqual(self.get_response.status_code, 200)
        self.assertTemplateUsed(self.get_response, 'cart.html')


class CartAddViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = create_product()
        user = create_user()
        shop = create_shop(user)
        shop_product = create_shop_product(shop, product)
        shop_2 = create_shop(user=create_user(email='test2@ya.ru'))
        shop_product_2 = create_shop_product(shop_2, product)

        cls.user = user
        cls.product = product
        cls.shop_product = shop_product
        cls.page_name_add = reverse(
            viewname='cart:cart_add',
            kwargs={'product_pk': product.id, 'shop_product_pk': shop_product.id}
        )
        cls.page_name_add_2 = reverse(
            viewname='cart:cart_add',
            kwargs={'product_pk': product.id, 'shop_product_pk': shop_product_2.id}
        )
        cls.page_name_random_add = reverse(
            viewname='cart:cart_random_add',
            kwargs={'product_pk': product.pk}
        )

    def test_cart_add(self):
        """
        Тест корректности добавления товара в корзину, тест слияния корзины после авторизации
        """
        ProductInCart.objects.create(user=self.user, product=self.product, shop_product=self.shop_product, quantity=1)

        response = self.client.post(self.page_name_add, data={'quantity': 1})
        self.assertRedirects(
            response=response,
            expected_url=reverse(viewname='product', kwargs={'slug': self.product.slug, 'pk': self.product.id})
        )
        self.assertEqual(ProductInCartAnon.objects.count(), 1)

        self.client.post(path=reverse(viewname='users:login'), data={'email': 'test@ya.ru', 'password': 'test1'})
        self.assertEqual(ProductInCartAnon.objects.count(), 0)
        user_cart = self.user.user_carts
        self.assertEqual(user_cart.count(), 1)
        self.assertEqual(user_cart.all()[0].quantity, 2)

    def test_save_cart_after_register(self):
        """
        Тест переноса корзины после регистрации
        """
        self.client.post(self.page_name_add, data={'quantity': 1})
        Group.objects.create(name='customer').save()
        self.client.post(
            path=reverse(viewname='users:register'),
            data={'email': 'test_user@ya.ru', 'password1': 'TestPass123', 'password2': 'TestPass123'}
        )
        user = self.client.request().context['user']
        self.assertEqual(user.user_carts.count(), 1)

    def test_change_seller(self):
        """
        Тест смены продавца в корзине при добавлении в корзину товара от другого продавца
        """
        self.client.force_login(user=self.user)
        self.client.post(self.page_name_add, data={'quantity': 3})
        self.client.post(self.page_name_add_2, data={'quantity': 1})

        user_cart = self.user.user_carts
        self.assertEqual(user_cart.count(), 1)
        self.assertEqual(user_cart.all()[0].quantity, 1)

    def test_cart_random_add(self):
        """
        Тест добавления товара в корзину без выбора продавца
        """
        self.client.force_login(user=self.user)
        self.client.post(path=self.page_name_random_add, data={'quantity': '1'})
        self.assertEqual(self.user.user_carts.count(), 1)

    def test_cart_random_add_invalid_quantity_value(self):
        """
        Тест не добавления товара в корзину без выбора продавца с невалидным значением кол-ва
        """
        self.client.force_login(user=self.user)
        self.client.post(path=self.page_name_random_add, data={'quantity': 'q'})
        self.assertEqual(self.user.user_carts.count(), 0)

    def test_save_cart_after_logout(self):
        """
        Тест сохранения корзины пользователя после выхода из системы
        """
        self.client.force_login(user=self.user)
        self.client.post(self.page_name_add, data={'quantity': 1})
        self.client.logout()

        self.assertEqual(self.user.user_carts.count(), 1)


class CartRemoveViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = create_user()
        product = create_product()
        shop_product = create_shop_product(create_shop(user), product)

        cls.user = user
        cls.page_name_add = reverse(
            viewname='cart:cart_add',
            kwargs={'product_pk': product.id, 'shop_product_pk': shop_product.id})
        cls.page_name_delete = reverse(viewname='cart:cart_remove', kwargs={'pk': product.id})

    def test_cart_remove_post(self):
        """
        Тест корректности удаления товара из корзины
        """
        self.client.post(self.page_name_add, data={'quantity': 1})
        response = self.client.post(self.page_name_delete)

        self.assertRedirects(response, reverse('cart:cart'))
        self.assertEqual(ProductInCartAnon.objects.count(), 0)

    def test_cart_remove_product_that_not_in_cart(self):
        """
        Тест появления ошибки при попытке удалить товар, которого нет в корзине у пользователя
        """
        self.client.force_login(user=self.user)
        response = self.client.post(self.page_name_delete)

        self.assertEqual(response.status_code, 404)
