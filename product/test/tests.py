from django.test import TestCase, Client
from django.urls import reverse_lazy

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
                (
                    'category', Category.objects.create(
                        name='test_category_{}'.format(i),
                        image='category.svg',
                    )
                 ),
                ('description', 'test_text'),
            )
        } for i in range(x)]

    def create_product(self, count: int = 1) -> Product | List[Product]:
        if count > 1:
            products: list = list()
            for data in self.data(count):
                products.append(
                    Product.objects.create(**data)
                )
            return products
        return Product.objects.create(**self.data(count)[0])

    def test_product_view(self) -> None:
        self.create_product(count=10)
        response = self.client.get(reverse_lazy('products'))
        self.assertTrue(response.status_code == 200)
