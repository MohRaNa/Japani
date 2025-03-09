from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('results/', views.search, name='search'),
    path('user/', views.user, name='user'),
    path('add-to-library/', views.add_to_library, name='add_to_library'),
]