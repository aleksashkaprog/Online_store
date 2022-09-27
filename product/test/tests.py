from django.test import TestCase, Client
from django.urls import reverse
from users.models import CustomUser
from product.models import Product
from category.models import Category

from typing import List, Callable


class ProductTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client: Client = Client()
        cls.user = CustomUser.objects.create_user(email='admin@ya.ru', password='TestPass12')
        cls.data: Callable = lambda x: [{
            key: value for key, value in (
                ('name', 'test_product_{}'.format(i)),
                ('price', (50 + i) * 10),
                ('old_price', (60 + i) * 10),
                (
                    'category', Category.objects.create(
                        name='test_category_{}'.format(i),
                        image='category.svg',
                    )
                ),
                ('description', 'test_text'),
            )
        } for i in range(x)]
        cls.products: List[Product] = [Product.objects.create(**data) for data in cls.data(x=10)]
        # cls.product_url = reverse('product', args=('test_product_1', 1))
        cls.login_url = reverse('users:login')
        cls.review = {'text': 'testreviewtext', 'rating': 3}

    def test_product_view(self) -> None:
        self.client.get(reverse('product', kwargs={'pk': 1}))
        self.client.get(reverse('product', kwargs={'pk': 1}))
        self.assertTemplateUsed('product/product.html')

    def test_add_review(self) -> None:
        self.client.login(username='admin@ya.ru', password='TestPass12')
        self.client.post(reverse('product', kwargs={'pk': 1}), self.review)
        self.client.get(reverse('product', kwargs={'pk': 1}))
        self.client.get(reverse('product', kwargs={'pk': 1}))
        # self.assertTrue(response.status_code == 200)
