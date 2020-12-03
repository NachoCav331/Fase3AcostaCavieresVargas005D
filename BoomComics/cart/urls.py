from django.urls import path
from .views import *

app_name = "cart"

urlpatterns = [
    path('add_product/<str:product_id>/', add_product, name='add_product'),
    path('remove_product/<str:product_id>/', remove_product, name='remove_product'),
    path('decrement_product/<str:product_id>/', decrement_product, name='decrement_product'),
    path('clear/', clear_cart, name='clear_cart'),
    path('pro/', procesar, name='procesar'),

    path('add_product_dc/<str:product_id>/', add_product_dc, name='add_product_dc'),
    path('remove_product_dc/<str:product_id>/', remove_product_dc, name='remove_product_dc'),
    path('decrement_product_dc/<str:product_id>/', decrement_product_dc, name='decrement_product_dc'),
    path('cleard/', clear_cart_dc, name='clear_cart_dc'),
    path('prod/', procesar_dc, name='procesar_dc'),


    path('add_product_marvel/<str:product_id>/', add_product_marvel, name='add_product_marvel'),
    path('remove_product_marvel/<str:product_id>/', remove_product_marvel, name='remove_product_marvel'),
    path('decrement_product_marvel/<str:product_id>/', decrement_product_marvel, name='decrement_product_marvel'),
    path('clearm/', clear_cart_marvel, name='clear_cart_marvel'),
    path('prom/', procesar_m, name='procesar_m'),


    path('add_product_manga/<str:product_id>/', add_product_manga, name='add_product_manga'),
    path('remove_product_manga/<str:product_id>/', remove_product_manga, name='remove_product_manga'),
    path('decrement_product_manga/<str:product_id>/', decrement_product_manga, name='decrement_product_manga'),
    path('clearma/', clear_cart_manga, name='clear_cart_manga'),
    path('proma/', procesar_ma, name='procesar_ma'),

]
