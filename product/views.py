from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView
from .models import Product
from .services import ProductService


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "product/product.html"

    def get_queryset(self):
        queryset = Product.objects.prefetch_related('reviews')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['user_review'] = ProductService.user_has_review(self.request.user, self.kwargs['pk'])
        return context

    def post(self, request, **kwargs):
        self.object = self.get_object()
        ProductService.review_form_save(instance=self, request=request)
        return redirect(reverse('product', args=(self.kwargs['slug'], self.kwargs['pk'])))
