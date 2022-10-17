from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import StepTwoForm, StepThreeForm


class OrderHistory(TemplateView):
    template_name = "order/historyorder.html"


class Order(TemplateView):
    template_name = "order/order.html"


class StepOne(TemplateView):
    template_name = "order/step_one.html"


class StepTwo(View):
    template_name = "order/step_two.html"

    def get(self, request, *args, **kwargs):
        form = StepTwoForm
        return render(request, self.template_name, {"form": form})


class StepThree(TemplateView):
    template_name = "order/step_three.html"

    def get(self, request, *args, **kwargs):
        form = StepThreeForm
        return render(request, self.template_name, {"form": form})


class StepFour(TemplateView):
    template_name = "order/step_four.html"
