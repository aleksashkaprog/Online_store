from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
