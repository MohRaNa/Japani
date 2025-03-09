from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests

def home(request):
    return render(request, 'index/index.html')

def search(request):
    query = request.GET.get('query')
    results = []

    if query:
        url = f'https://api.jikan.moe/v4/anime?q={query}'
        response = requests.get(url)

    if response.status_code == 200:
            data = response.json()
            results = data.get('data', [])
    
    return render(request, 'search/search.html', {'results': results,'query': query})

def user(request):
    return render(request, 'user/library.html')

@login_required(login_url='login')
def add_to_library(request):
    if request.method == 'POST':
        mal_id = request.POST.get('mal_id')
        title = request.POST.get('title')
        image_url = request.POST.get('image_url')
        synopsis = request.POST.get('synopsis')
        url = request.POST.get('url')

        # Verifica si el anime ya está en la librería del usuario
        if not UserLibrary.objects.filter(user=request.user, mal_id=mal_id).exists():
            # Agrega el anime a la librería del usuario
            UserLibrary.objects.create(
                user=request.user,
                mal_id=mal_id,
                title=title,
                image_url=image_url,
                synopsis=synopsis,
                url=url
            )

        return redirect('search')  # Redirige de vuelta a la página de búsqueda
    else:
        return redirect('home')  # Si no es una solicitud POST, redirige al inicio