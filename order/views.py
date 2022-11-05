from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
import datetime
from .models import Order
from .forms import StepOneForm, StepTwoForm, StepThreeForm


class OrderHistory(TemplateView):
    template_name = "order/historyorder.html"


class OrderView(TemplateView):
    template_name = "order/order.html"


class StepOne(View):
    template_name = "order/step_one.html"

    def get(self, request, *args, **kwargs):
        form = StepOneForm
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = StepOneForm(request.POST)
        order = Order.objects.create(consumer=request.user, order_in=False)
        if form.is_valid():
            order.first_second_names = form.cleaned_data["first_second_names"]
            order.email = form.cleaned_data["email"]
            order.phone = form.cleaned_data["phone"]
            order.save()
            return redirect("order-step-two")
        return render(request, self.template_name, {"form": form})


class StepTwo(View):
    template_name = "order/step_two.html"

    def get(self, request, *args, **kwargs):
        form = StepTwoForm
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = StepOneForm(request.POST)
        order = Order.objects.get(consumer=request.user, order_in=False)
        if form.is_valid():
            order.delivery = form.cleaned_data["delivery"]
            order.city = form.cleaned_data["city"]
            order.address = form.cleaned_data["address"]
            order.save()
            return redirect("order-step-three")
        return render(request, self.template_name, {"form": form})


class StepThree(TemplateView):
    template_name = "order/step_three.html"

    def get(self, request, *args, **kwargs):
        form = StepThreeForm
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = StepOneForm(request.POST)
        order = Order.objects.get(consumer=request.user, order_in=False)
        if form.is_valid():
            order.payment = form.cleaned_data["payment_method"]
            order.order_in = True
            order.ordered = datetime.datetime.today()
            return redirect("order-step-four")
        return render(request, self.template_name, {"form": form})


class StepFour(View):
    template_name = "order/step_four.html"

    def get(self, request, *args, **kwargs):
        order = Order.objects.filter(consumer=request.user, order_in=True).last()
        return render(request, self.template_name, {"order": order})
        # return render(request, self.template_name)
