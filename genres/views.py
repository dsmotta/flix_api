import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from genres.models import Genre

@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id':genre.id, 'name':genre.name} for genre in genres ] #Serializando uma lista
        return JsonResponse(data, safe=False) # a resposa Json sera a variavel serializada
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) # captura os dados da requisição tranforma em dicionario ja formatado
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name}, status=201,
        )

@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method =='GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)

    elif request.method =='PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {'id': genre.id, 'name': genre.name}
        )
    
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': 'Gênero excluido com sucesso...'}, status=204
        )



