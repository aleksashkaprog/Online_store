# from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class AccountView(TemplateView):
    template_name = 'users/account.html'


class ProfileView(TemplateView):
    template_name = 'users/profile.html'
