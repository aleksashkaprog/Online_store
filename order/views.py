# from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class OrderHistory(TemplateView):
    template_name = 'order/historyorder.html'


class Order(TemplateView):
    template_name = 'order/order.html'
