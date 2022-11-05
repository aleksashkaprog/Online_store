from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass
