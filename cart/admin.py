from django.contrib import admin

from .models import ProductInCart, ProductInCartAnon


@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductInCartAnon)
class ProductInCartAnonAdmin(admin.ModelAdmin):
    pass
