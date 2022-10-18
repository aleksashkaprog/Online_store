from django.contrib import admin
from . import models


@admin.register(models.Favourite)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DayOffer)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Hot)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Limit)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Top)
class CategoryModelAdmin(admin.ModelAdmin):
    pass



