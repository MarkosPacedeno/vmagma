from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('acerca/', views.acerca, name='acerca'),
    path('noticias/', views.noticias, name='noticias'),
    path('personajes/', views.personajes, name='personajes'),
    path('blog/', views.blog, name='blog'),



] 


