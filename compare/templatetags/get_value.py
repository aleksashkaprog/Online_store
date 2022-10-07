from django.template import Library
from django.utils.translation import gettext_lazy as _


register = Library()


@register.filter(name='get_value')
def get_value(dct: dict, key) -> str:
    """Получение значения из словаря по ключу в шаблоне."""
    return dct.get(key, _('Нет информации'))
