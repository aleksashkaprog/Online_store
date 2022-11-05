from typing import Optional


class CatalogMixin:

    def get_queryset(self):
        queryset = super().get_queryset().select_related('category').prefetch_related('property')
        return queryset


class CatalogOrderByMixin:

    field: Optional[str] = None

    def get_queryset(self):
        queryset = super().get_queryset().order_by(self.field)
        return queryset


class SearchMixin:

    def get_queryset(self):
        queryset = super().get_queryset().filter(name__contains=self.request.GET.get('query', ''))
        return queryset
