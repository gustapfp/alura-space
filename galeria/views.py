from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografias
# Create your views here.
def index(request): 
    fotografias = Fotografias.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"card":fotografias})

def imagem(request, foto_id): 
    fotografias = get_object_or_404(Fotografias, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografias": fotografias})