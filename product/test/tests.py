from django.test import TestCase, Client

from django.urls import reverse

from product.models import Product
from category.models import Category

from typing import List, Callable


class ProductTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client: Client = Client()
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

    def test_product_view(self) -> None:
        response = self.client.get(reverse('products'))
        self.assertTrue(response.status_code == 200)
