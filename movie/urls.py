from django.urls import path
from movie.views import ListaPeliculas, DetallePelicula

urlpatterns = [
    path( '', ListaPeliculas.as_view(), name='listPeliculas'),
    path('peliculas/<int:pk>/', DetallePelicula.as_view(), name='detalle_pelicula'),  # Nueva ruta

]