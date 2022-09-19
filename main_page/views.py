from django.shortcuts import render
from category.services import CategoryService


def about(request):
    categories = CategoryService.get_categories()
    return render(request, 'about_market.html', {'categories': categories, })


def contacts(request):
    categories = CategoryService.get_categories()
    return render(request, 'contacts.html', {'categories': categories, })


def main_page(request):
    categories = CategoryService.get_categories()
    return render(request, "main_page.html", {'categories': categories, })
