from django.shortcuts import render , redirect
from catalogo.models import Comic
from .cart import Cart
from django.contrib import messages
# Create your views here.

#acciones carro index
def add_product(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.add(comic=comic)
    return redirect("index")

def remove_product(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.remove(comic)
    return redirect("index")

def decrement_product(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.decrement(comic=comic)
    return redirect("index")

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("index")

def procesar(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Su compra a sido realizada con exito!')
    return redirect("index")

#acciones carro DC
def add_product_dc(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.add(comic=comic)
    return redirect('/catalogo/DC/2')

def remove_product_dc(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.remove(comic)
    return redirect('/catalogo/DC/2')

def decrement_product_dc(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.decrement(comic=comic)
    return redirect('/catalogo/DC/2')

def clear_cart_dc(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/catalogo/DC/2')

def procesar_dc(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Su compra a sido realizada con exito!')
    return redirect('/catalogo/DC/2')  

#acciones carro MARVEL
def add_product_marvel(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.add(comic=comic)
    return redirect('/catalogo/MARVEL/3')

def remove_product_marvel(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.remove(comic)
    return redirect('/catalogo/MARVEL/3')

def decrement_product_marvel(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.decrement(comic=comic)
    return redirect('/catalogo/MARVEL/3')

def clear_cart_marvel(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/catalogo/MARVEL/3')

def procesar_m(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Su compra a sido realizada con exito!')
    return redirect('/catalogo/MARVEL/3')

#acciones carro manga
def add_product_manga(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.add(comic=comic)
    return redirect('/catalogo/Mangas/1')

def remove_product_manga(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.remove(comic)
    return redirect('/catalogo/Mangas/1')

def decrement_product_manga(request, product_id):
    cart = Cart(request)
    comic = Comic.objects.get(id=product_id)
    cart.decrement(comic=comic)
    return redirect('/catalogo/Mangas/1')

def clear_cart_manga(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/catalogo/Mangas/1')

def procesar_ma(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Su compra a sido realizada con exito!')
    return redirect('/catalogo/Mangas/1')
