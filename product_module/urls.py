from os import name

from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductListView.as_view(), name = 'product-list'),
    path('cat/<cat>', views.ProductListView.as_view(), name = 'product-categories-list'),
    path('<slug:slug>', views.ProductDetaiView.as_view(), name = 'product-detail')


]