from django.utils import timezone
from django.db.models import Q


def get_discounts_queryset(discounts_model):
    discounts = discounts_model.objects.filter(Q(end__gte=timezone.now()) | Q(end=None), active=True)
    return discounts
