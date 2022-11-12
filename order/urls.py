from django.urls import path
from .views import OrderHistory, OrderView, StepOne, StepTwo, StepThree, StepFour

urlpatterns = [
    path("history/", OrderHistory.as_view(), name="history-order"),
    path("history/<int:order_pk>/", OrderView.as_view(), name="one-order"),
    path("step1/", StepOne.as_view(), name="order-step-one"),
    path("step2/", StepTwo.as_view(), name="order-step-two"),
    path("step3/", StepThree.as_view(), name="order-step-three"),
    path("step4/", StepFour.as_view(), name="order-step-four"),
]
