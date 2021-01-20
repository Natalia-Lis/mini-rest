from rest_framework import serializers
from .models import Movies


class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'name', 'director')