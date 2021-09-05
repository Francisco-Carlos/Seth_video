from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    Nikename = models.CharField(max_length=200)
    Foto = models.ImageField(upload_to='Fotos/%d/%m%Y')
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Videos(models.Model):
    Usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    Video = models.FileField(upload_to='VideosUser/%d/%m%y')
    Titulo = models.CharField(max_length=200)
    Descricao = models.TextField(max_length=400, blank=True)
    Categoria = models.CharField(max_length=200)
    
class Comentarios(models.Model):
    Usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    Video = models.ForeignKey(Videos,on_delete=models.CASCADE)
    Comentario = models.TextField(max_length=500)

