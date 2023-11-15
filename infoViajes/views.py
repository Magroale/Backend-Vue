from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from bson import ObjectId
# Create your views here.

from infoViajes.models import Viaje
from infoViajes.serializers import ViajeSerializer

from infoViajes.models import Comentario
from infoViajes.serializers import ComentarioSerializer

def home_page(request):
    if request.method == 'GET':
        viaje = Viaje.objects.all()
        viaje_serializer = ViajeSerializer(viaje, many=True)
        return JsonResponse(viaje_serializer.data, safe=False)
    
def vista_comentario(request):
    if request.method == 'GET':
        comment = Comentario.objects.all()
        comment_serializer = ComentarioSerializer(comment, many=True)
        return JsonResponse(comment_serializer.data, safe=False)