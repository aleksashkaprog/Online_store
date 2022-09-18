from django.test import TestCase
from django.db.models import QuerySet

from category.models import Category

from typing import List, Callable


class CategoryTestCase(TestCase):
    """Класс тестирования модели Category на создание и получение объектов"""
    def setUp(self) -> None:
        self.category: QuerySet = Category.objects.all()
        self.data: Callable = lambda x: [{
            key: '{}'.format(value) for key, value in (
                ('name', 'test_name_{}'.format(i)),
                ('image', 'test_file_{}.png'.format(i))
            )
        } for i in range(x)]

    def create_category(self, count: int = 1) -> Category | List[Category]:
        if count > 1:
            categories: list = list()
            for data in self.data(count):
                categories.append(
                    Category.objects.create(**data)
                )
            return categories
        return Category.objects.create(**self.data()[0])

    def test_create_category(self) -> None:
        for i, data in enumerate(self.data(10)):
            with self.subTest(i=i):
                category = Category.objects.create(**data)
                self.assertTrue(type(category), Category)

    def test_get_category(self) -> None:
        categories = self.create_category(count=10)
        self.assertTrue(len(categories) == 10)
