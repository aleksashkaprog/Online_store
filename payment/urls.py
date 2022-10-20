from django.urls import path

from .views import PaymentAPIView


app_name = 'payment'

urlpatterns = [
    path('<int:order_id>/<int:card_number>/<str:cost>/', PaymentAPIView.as_view(), name='pay'),
]
