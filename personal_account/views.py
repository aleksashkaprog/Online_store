# from django.shortcuts import render
# from django.shortcuts import render
# from django.views import View
from django.views.generic import TemplateView


class AccountView(TemplateView):
    template_name = 'users/account.html'


class ProfileView(TemplateView):
    template_name = 'users/profile.html'
