from django.shortcuts import render
from rest_framework import viewsets

from .models import Movies
from .serializers import MoviesSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all().order_by('name')
    serializer_class = MoviesSerializer