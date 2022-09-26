from django.contrib import admin
from .models import Product, Review, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    exclude = ['id']
    inlines = [ImageInline]
    list_display = ['id', 'category', 'name', 'price']


admin.site.register(Product, ProductAdmin)

admin.site.register(Review)
