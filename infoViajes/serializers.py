from rest_framework import serializers
from infoViajes.models import Viaje
from infoViajes.models import Comentario

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = ('_id','country','location','score','discount','discountPercentage','price','numberDays','news')
        
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('_id','text_Comments','personName')