from django import forms  #incorpora los formualrios de django
from apps.productos.models import producto,categoria

class ProductoForm(forms.ModelForm):
	class Meta: 
		model = producto 

		fields= [  #los mismos del modelo
		'nombre' ,
		'descripcion',
		'costo' ,
		'disponible',
		'numeroExistencias',
		'categoria',

		]
		labels={
		'nombre' : 'Nombre',

		'descripcion': 'Descripcion del Producto',
		'costo' : 'Costo',
		'disponible': 'Disponible',
		'numeroExistencias': 'Numero de Existencias',
		'categoria': 'Categoria',

		}

		Choices={
		("enlatados","enlatados"),
		("lacteos","lacteos"),
		("abarrotes","abarrotes")
		}
		widget={
		'nombre' : forms.TextInput(),

		'descripcion':forms.TextInput(),
		'costo' : forms.FloatField(),
		'disponible': forms.widgets.CheckboxInput(),
		'numeroExistencias': forms.IntegerField(),
		'categoria': forms.ChoiceField(choices=Choices),

		}

class CategoriaForm(forms.ModelForm):
	class Meta: 
		model = categoria 

		fields= [  #los mismos del modelo
		'categoria' ,
		'fechaCreacion',
		

		]
		labels={
		'categoria' : 'Nombre',
		'fechaCreacion': 'Fecha Creacion',
		

		}

		
		widget={
		'categoria' : forms.TextInput(),
		'fechaCreacion' : forms.TextInput(),

		

		}

		