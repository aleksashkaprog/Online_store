from django.urls import path

from . import views


urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('add/<int:pk>/', views.CatalogView.add_to_compare, name='add_to_compare')
]
