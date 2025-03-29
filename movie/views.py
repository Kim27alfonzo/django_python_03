
from django.views.generic import ListView
from django.views.generic import DetailView
from movie.models import Pelicula

class ListaPeliculas(ListView):
    model = Pelicula
    template_name = 'listPelicula.html'
    context_object_name = 'peliculas'

class DetallePelicula(DetailView):
    model = Pelicula
    template_name = 'detalle_pelicula.html'
    context_object_name = 'pelicula'

class MovieDetailView(DetailView):
    model = Pelicula
    template_name = 'movie/movie_detail.html'
    context_object_name = 'movie'

