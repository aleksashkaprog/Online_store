# import random
import datetime
import random

from django.shortcuts import render
from django.views import View

from catalog.models import Favourite, DayOffer, Top, Hot, Limit
from main_page.models import Banner


# from main_page.models import Banner


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
        day_offer = DayOffer.objects.filter(day=datetime.date.today())
        top_products = Top.objects.all()
        hot_offers = Hot.objects.all()
        limited_offers = Limit.objects.all()
        context = {
            'banners': banners,
            'favourite_categories': favourite_categories,
            'day_offer': day_offer,
            'top_products': top_products,
            'hot_offers': hot_offers,
            'limited_offers': limited_offers
        }
        return render(request, 'main_page.html', context)
