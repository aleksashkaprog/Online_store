from django.test import TestCase

from product.models import Product
from category.models import Category

from typing import List, Callable


class ProductTestCase(TestCase):
    """Класс тестирования модели Product на создание и получение объектов."""
    def setUp(self) -> None:
        self.category = Category.objects.create(
            name='test_category',
            image='category.svg',
        )
        self.data: Callable = lambda x: [{
            key: value for key, value in (
                ('name', 'test_product_{}'.format(i)),
                ('price', (50 + i) * 10),
                ('category', self.category),
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

    def test_create_product(self) -> None:
        for i, data in enumerate(self.data(10)):
            with self.subTest(i=i):
                product = Product.objects.create(**data)
                self.assertTrue(type(product) == Product)

    def test_get_product(self) -> None:
        products = self.create_product(count=10)
        self.assertTrue(len(products) == 10)
