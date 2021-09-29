from django.shortcuts import render

def publicacion_lista(request):
    return render(request, 'blog/publicacion_lista.html', {})