from django.shortcuts import render
from . models import Comic, Autor, Formato, Tipo
from django.views import generic
from cart.cart import Cart

from django.core.paginator import Paginator
from django.http import Http404

from django.views.generic.edit import CreateView, UpdateView ,DeleteView
from django.urls import reverse_lazy
from .forms import ComicsForms

# Create your views here.

def index(request):
    cart = Cart(request)
    comics_list = Comic.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(comics_list, 12)
        comics_list = paginator.page(page)
    except:
        raise Http404
    data = {

        'entity': comics_list,
        'paginator': paginator
    }    
    return render(
        request,  
        'index.html', data
    )   

# vista que lee los mangas
def mangas(request, tip_list):
    cart = Cart(request)
    tip_list = Comic.objects.filter(tipo=1)
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(tip_list, 12)
        tip_list = paginator.page(page)
    except:
        raise Http404

    data = {

        'entity': tip_list,
        'paginator': paginator
    }    
    return render(
        request,  
        'manga.html', data
    )   

# vista que lee los comics de dc
def dc(request, tip_dc):
    cart = Cart(request)
    tip_dc = Comic.objects.filter(tipo=2)
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(tip_dc, 12)
        tip_dc = paginator.page(page)
    except:
        raise Http404
    data = {

        'entity': tip_dc,
        'paginator': paginator
    }    
    return render(
        request,  
        'dc.html', data
    )   

# vista que lee los comics de marvel
def marvel(request, tip_m):
    cart = Cart(request)
    tip_m = Comic.objects.filter(tipo=3)
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(tip_m, 12)
        tip_m = paginator.page(page)
    except:
        raise Http404
    data = {

        'entity': tip_m,
        'paginator': paginator
    }    
    return render(
        request,  
        'marvel.html', data
    )   
def contacto(request):
    
    return render(
        request,
        'contacto.html',
    )

#CRUD de tabala Comic
class ComicCreate(CreateView):
    model = Comic
    form_class = ComicsForms
    

class ComicUpdate(UpdateView):
    model = Comic
    form_class = ComicsForms
    

class ComicDelete(DeleteView):
    model= Comic
    success_url = reverse_lazy('index')

class ComicDetailView(generic.DetailView):
    model = Comic
#CRUD AUTOR
class AutorCreate(CreateView):
    model = Autor
    fields ='__all__'
class AutorDelete(DeleteView):
    model= Autor
    success_url = reverse_lazy('index')
class AutorDetailView(generic.DetailView):
    model = Autor
class AutorListView(generic.ListView):
    queryset= Autor.objects.all().order_by('pk')