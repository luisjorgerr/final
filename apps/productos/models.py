from django.db import models

# Create your models here.


class categoria(models.Model):
	categoria=models.CharField(max_length=30)
	fechaCreacion=models.DateField(default='2000-01-01')
	
class producto(models.Model):
	nombre=models.CharField(max_length=30)
	descripcion=models.CharField(max_length=100)
	costo=models.FloatField(default=0.0)
	disponible=models.BooleanField(default=0)
	numeroExistencias=models.IntegerField(default=0)
	categoria=models.ForeignKey(categoria,null=True,blank=True, on_delete=models.DO_NOTHING)

