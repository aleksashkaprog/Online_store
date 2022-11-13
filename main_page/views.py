import datetime
import random
from product.models import Product
from django.shortcuts import render
from django.views import View
from administration.models import Cache
from catalog.models import Favourite, DayOffer, Top, Hot, Limit
from main_page.models import Banner
from discount.models import ProductDiscount
from discount.services import get_discounts_queryset


class MainPageView(View):

    def get(self, request):
        banner_list = []
        banner = Banner.objects.all()
        if banner:
            for ban in banner:
                banner_list.append(ban)
            banners = random.sample(banner_list, 3)
        else:
            banners = None
        if request.user:
            favourite_categories = Favourite.objects.filter(user=request.user.id)
        else:
            favourite_categories = None
        day_offer = DayOffer.objects.first()
        top_products = Top.objects.all()[:8]
        active_discounts = get_discounts_queryset(ProductDiscount)
        hot_offers = Product.objects.filter(discounts__discount__in=active_discounts)
        limited_offers = Limit.objects.all()
        main_cache = Cache.objects.get(name='Main cache').value
        context = {
            'banners': banners,
            'favourite_categories': favourite_categories,
            'day_offer': day_offer,
            'top_products': top_products,
            'hot_offers': hot_offers,
            'limited_offers': limited_offers,
            'main_cache': main_cache,
        }
        return render(request, 'main_page/main_page.html', context)


class ContactsView(View):
    def get(self, request):
        return render(request, 'main_page/contacts.html')