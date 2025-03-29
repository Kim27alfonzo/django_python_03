from django.urls import path
from movie.views import ListaPeliculas, DetallePelicula, MovieDetailView

urlpatterns = [
    path( '', ListaPeliculas.as_view(), name='listPeliculas'),
    path('peliculas/<int:pk>/', DetallePelicula.as_view(), name='detalle_pelicula'),  # Nueva ruta
    path('movie/detail/<int:pk>/', MovieDetailView.as_view(), name='movie'),  # Ruta de

]