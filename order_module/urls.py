from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.add_to_order, name='add_product_to_order'),
]