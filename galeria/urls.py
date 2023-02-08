from galeria.views import index, imagem, buscar
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar")
    
]