from django.views.generic import TemplateView


class Product(TemplateView):
    template_name = "inc/product/good_detail.html"
