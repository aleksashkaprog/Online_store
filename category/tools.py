from typing import Type
from transliterate import detect_language, translit

from . import models


def get_path(instance: Type['models.Category'], filename: str) -> str:
    file_type: str = filename.split('.')[-1]
    return '{}/{}.{}'.format(
        'category',
        instance.name,
        file_type,
    )


def get_slug(name: str) -> str:
    slug: str = name
    if detect_language(name) == 'ru':
        slug = translit(name, 'en')
    return slug
