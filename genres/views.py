from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer



# usando class Based Views - Generic Views 
class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Usando function views
# @csrf_exempt
# def  genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id':genre.id, 'name':genre.name} for genre in genres ] #Serializando uma lista
#         return JsonResponse(data, safe=False) # a resposa Json sera a variavel serializada
#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8')) # captura os dados da requisição tranforma em dicionario ja formatado
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {'id': new_genre.id, 'name': new_genre.name}, status=201,
#         )


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# @csrf_exempt
# def genre_detail_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)

#     if request.method =='GET':
#         data = {'id': genre.id, 'name': genre.name}
#         return JsonResponse(data)

#     elif request.method =='PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {'id': genre.id, 'name': genre.name}
#         )
    
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse(
#             {'message': 'Gênero excluido com sucesso...'}, status=204
#         )



