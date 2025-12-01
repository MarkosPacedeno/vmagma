from django.db import models

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"

from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True) 

    def __str__(self):
        return self.titulo