from django.db.models import Avg, Min, Max


class ProductRatingMixin:
    """Класс миксин. Добавляет метод дечернему классу."""

    @property
    def rating(self) -> int:
        return self.reviews.aggregate(Avg('rating')).get('rating__avg')


class ProductPriceMixin:
    """Класс миксин. Добавляет метод дечернему классу."""

    @property
    def price(self):
        return self.shop_products.aggregate(Min('price')).get('price__min')

    @property
    def old_price(self):
        return self.shop_products.aggregate(Max('old_price')).get('old_price__max')
