from django.test import TestCase
from django.urls import reverse

from product.models import Product
from category.models import Category


class CatalogTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.category = Category.objects.create(
            name='test_name',
            image='file.svg'
        )
        cls.products: list = [Product.objects.create(
            name='test_name_{}'.format(_),
            price=(60 + _) * 10,
            old_price=(70 + _) * 10,
            category=cls.category,
        ) for _ in range(10)]

    def test_catalog_get(self) -> None:
        response = self.client.get(reverse('catalog'))
        self.assertTrue(response.status_code == 200)

    def test_catalog_add_to_compare(self) -> None:
        for i, product in enumerate(self.products):
            with self.subTest(i=i):
                response = self.client.get(reverse('add_to_compare', kwargs={'pk': i}))
                self.assertRedirects(response, reverse('catalog'))
