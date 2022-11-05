from product.models import Product

from . import services


class CatalogView(services.CatalogProductService):

    template_name = 'catalog.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 2


class CatalogOrderByDateView(services.CatalogProductOrderByService, CatalogView):

    field = '-created_at'


class CatalogOrderByViewsView(services.CatalogProductOrderByService, CatalogView):

    field = 'views'


class CatalogCategoryView(services.CatalogCategoryService):

    template_name = 'catalog.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 2


class CatalogCategoryOrderByDateView(services.CatalogCategoryOrderByService, CatalogCategoryView):

    field = '-created_at'


class CatalogCategoryOrderByViewsView(services.CatalogCategoryOrderByService, CatalogCategoryView):

    field = 'views'
