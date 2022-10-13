from django.urls import path
from .views import AccountView, ProfileView, HistoryView

urlpatterns = [
    path("", AccountView.as_view(), name="account"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("history/", HistoryView.as_view(), name='history-view')
]
