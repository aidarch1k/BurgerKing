from django.urls import path
from menu.views import index, product_list, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('product-list/<str:slug>/', product_list, name='list'),
    path('product/<int:product_id>/', product_detail, name='detail'),
]