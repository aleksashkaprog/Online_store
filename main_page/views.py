# import random

from django.shortcuts import render
from django.views import View

# from main_page.models import Banner


class MainPageView(View):

    def get(self, request):
        # banner_list = []
        # banner = Banner.objects.all()
        # for ban in banner:
        #     banner_list.append(ban)
        # my_banner = random.sample(banner_list, 3)
        my_banner = None
        return render(request, 'main_page.html', context={'banners': my_banner})
