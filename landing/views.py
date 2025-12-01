from django.shortcuts import render
from .models import Noticia
from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm

def index(request):
    return render(request, 'landing/index.html')

def galeria(request):
    return render(request, 'landing/galeria.html')

def acerca(request):
    return render(request, 'landing/acerca.html')

def noticias(request):
    return render(request, 'landing/noticias.html')

def personajes(request):
    return render(request, 'landing/personajes.html')

def blog(request):
    comentarios = Comentario.objects.order_by('-fecha')
    form = ComentarioForm()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')

    return render(request, 'landing/blog.html', {
        'comentarios': comentarios,
        'form': form
    })

def noticias(request):
    noticias = Noticia.objects.order_by('-fecha')
    return render(request, 'landing/noticias.html', {'noticias': noticias})
