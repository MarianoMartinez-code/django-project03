from django.shortcuts import render
from django.views.generic import ListView, DetailView
from movies.models import Pelicula

# Create your views here.

class MovieListView(ListView):
    model = Pelicula
    template_name = "movies/movie_list.html"
