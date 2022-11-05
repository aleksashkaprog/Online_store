from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView

from .models import Product, Review
from .services import ProductService
from cart.forms import CartAddProductForm


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "product/product.html"

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('reviews__user', 'shop_products__store', 'images')
        return queryset

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['user_review'] = ProductService.user_has_review(self.request.user, self.object)
        context['form'] = CartAddProductForm()
        reviews = Review.objects.filter(product=self.object)
        paginator = Paginator(reviews, 1)
        page = self.request.GET.get('page')
        context['reviews'] = paginator.get_page(page)
        context['paginator'] = paginator
        return context

    def post(self, request, **kwargs):
        self.object = self.get_object()
        ProductService.review_form_save(instance=self, request=request)
        return redirect(reverse(viewname='product', kwargs={'slug': self.kwargs['slug']}))
