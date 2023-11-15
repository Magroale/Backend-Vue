from django.db import models
from djongo import models as mongo_models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Comentario(models.Model):
    _id = mongo_models.ObjectIdField(primary_key = True)
    text_Comments = models.TextField(max_length=2000)
    personName = models.CharField(max_length=2000)
    
    class Meta:
        db_table = 'Comentarios'
class Viaje(models.Model):
        
    _id = mongo_models.ObjectIdField(primary_key = True)
    country = models.CharField(max_length=2000)
    location = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(limit_value=0),MaxValueValidator(limit_value=5)])
    discount = models.BooleanField(default=False)
    discountPercentage = models.DecimalField(max_digits=2, decimal_places=2, validators=[MinValueValidator(limit_value=0),MaxValueValidator(limit_value=1)])
    price = models.IntegerField()
    numberDays = models.IntegerField(validators=[MaxValueValidator(limit_value=30)])
    news = models.TextField(max_length=2000)
    image = mongo_models.ImageField()
    
    class Meta:
        db_table = 'Viajes'
        
    
        

