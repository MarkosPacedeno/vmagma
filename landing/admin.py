from django.contrib import admin
from .models import Comentario, Noticia

admin.site.register(Comentario)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'contenido')

admin.site.register(Noticia, NoticiaAdmin)
