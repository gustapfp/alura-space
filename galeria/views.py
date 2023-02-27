from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografias
from django.contrib import auth, messages
# Create your views here.
def index(request): 
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    fotografias = Fotografias.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"card":fotografias})

def imagem(request, foto_id): 
    fotografias = get_object_or_404(Fotografias, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografias": fotografias})

def buscar(request):
    fotografias = Fotografias.objects.order_by("data_fotografia").filter(publicada=True) 
    if "buscar" in request.GET:
        foto_buscada = request.GET["buscar"]
        if foto_buscada:
            fotografias = fotografias.filter(nome__icontains = foto_buscada)

    return render(request, "galeria/buscar.html", {"card":fotografias})