from typing import Type
from transliterate import detect_language, translit

from . import models


def get_path(instance: Type['models.Category'], filename: str) -> str:
    """Возращает путь к файлу."""
    file_type: str = filename.split('.')[-1]
    return '{}/{}.{}'.format(
        'category',
        instance.name,
        file_type,
    )


def get_slug(name: str) -> str:
    """Возвращает строку slug."""
    # написать валидатор на корректность ввода языка
    slug: str = name
    if detect_language(name) == 'ru':
        slug = translit(name, reversed=True)
    return '-'.join(slug.split()).lower().replace(')', '').replace('(', '')
