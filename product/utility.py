from django.db.models import Avg


class ProductRatingMixin:
    """Класс миксин. Добавляет метод дечернему классу."""

    @property
    def rating(self: 'product.models.Product') -> int:
        return self.reviews.aggregate(Avg('rating')).get('rating__avg', 0)
