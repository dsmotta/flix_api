from rest_framework import serializers
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


# Exemplo de uso serializer.Serializer feito manualmente
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
#     release_date = serializers.DateField()
#     actor = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
#     resume = serializers.CharField()


# Exemplo de uso do serializer.ModelSerializer
class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
   
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1990')
        return value
    
    def validate_resume(self, value):
        print(value)
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True) # adciona um campo calculado (MethodField)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
         rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
         if rate:
             return round(rate, 1)
         return None