from django.db import models
from datetime import datetime

# Create your models here.
class Fotografias(models.Model): 
    OPCOES_CATEGORIAS = (
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=250, null=False, blank=False)
    categoria = models.CharField(max_length=12, choices=OPCOES_CATEGORIAS, default="")
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    imagem = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)

    def __str__(self) -> str:
        return  self.nome