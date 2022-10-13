# from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from personal_account.models import ViewsHistory


# Create your views here.

class AccountView(TemplateView):
    template_name = 'users/account.html'


class ProfileView(TemplateView):
    template_name = 'users/profile.html'


class HistoryView(View):
    def get(self, request):
        viewed_product = ViewsHistory.objects.filter(user=request.user.id)
        context = {
            'viewed_product': viewed_product
        }
        return render(request, 'view_history.html', context)
