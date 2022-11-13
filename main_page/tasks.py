from celery import shared_task
from .models import Banner
from random import randint


@shared_task()
def day_offer_update():
    pass