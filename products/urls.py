from django.urls import path
from .views import get_products,add_product,update_product, delete_product



urlpatterns = [
    path('getproducts/', get_products, name='getproducts'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product')
]
