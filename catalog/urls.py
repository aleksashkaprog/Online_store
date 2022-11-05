from django.urls import path

from . import views


urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('order_by_date/', views.CatalogOrderByDateView.as_view(), name='catalog_order_by_date'),
    path('order_by_views/', views.CatalogOrderByViewsView.as_view(), name='catalog_order_views'),
    path('category/<slug:slug>/', views.CatalogCategoryView.as_view(), name='catalog_category'),
    path('category_order_by_date/<slug:slug>/', views.CatalogOrderByDateView.as_view(),
         name='catalog_category_order_by_date'),
    path('category_order_by_views/<slug:slug>/', views.CatalogOrderByViewsView.as_view(),
         name='catalog_category_order_by_views'),
    path('add/<int:pk>/', views.CatalogView.add_to_compare, name='add_to_compare')
]
