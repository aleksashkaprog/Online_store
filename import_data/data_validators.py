"""Модели из модуля pydantic для валидации импортируемых json данных"""

from pydantic import BaseModel
from typing import Dict, Union


class Property(BaseModel):
    name: str


class ProductProperty(BaseModel):
    property: Property
    value: str


class Product(BaseModel):
    name: str
    category: str
    description: str
    properties: list[ProductProperty]


class Shop(BaseModel):
    name: str
    address: str
    email: str
    phone: str
    description: str
    slug: str


class ProductShopData(BaseModel):
    objects: Dict[str, Dict[str, Union[Product, Shop]]]
