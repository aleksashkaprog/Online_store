from django.db.models import Avg


class ProductMixin:
    """Класс миксин. Добавляет метод дечернему классу."""

    @property
    def rating(self) -> int:
        return self.reviews.aggregate(Avg('rating')).get('rating__avg', 0)

    @property
    def discount(self):
        """Отображает приоритетную скидку на продукт в текстовом варианте,
        в зависимости от механизма рассчета скидки"""
        discount_display = None
        from discount.services import get_product_discount
        discount = get_product_discount(self)
        if discount:
            if discount.type == 'percent':
                discount_display = f'-{int(discount.value)}%'
            elif discount.type == 'sum':
                discount_display = f'-{int(discount.value)}'
            else:
                discount_display = int(discount.value)

        return discount_display
