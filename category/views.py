from django.shortcuts import render

from . import models


def category(request):
    categories = models.Category.objects.all()
    return render(request, 'base.html', {'categories': categories, })
