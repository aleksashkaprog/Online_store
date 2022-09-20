from django.test import TestCase, Client
from django.db.models import QuerySet
from django.urls import reverse_lazy

from category.models import Category

from typing import List, Callable


class CategoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client: Client = Client()
        cls.category: QuerySet = Category.objects.all()
        cls.data: Callable = lambda x: [{
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
        return Category.objects.create(**self.data(x=count)[0])

    def test_category_view(self) -> None:
        self.create_category(count=10)
        response = self.client.get(reverse_lazy('category'))
        self.assertTrue(response.status_code == 200)
