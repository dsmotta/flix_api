from django.contrib import admin
from genres.models import Genre #importando a classe do model

# registro do model para ser manipulado no /adim do django

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name')
