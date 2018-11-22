from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from apps.productos.models import producto,categoria
from django.views.generic.list import ListView
from django.template import Context, loader
from django.views.generic.base import TemplateView
from apps.productos.formulario import ProductoForm,CategoriaForm
from django.db.models import F,Sum
from collections import Counter
#from apps.productos.formulario import ProductoForm,CategoriaForm
# Create your views here.

#def index(request):
#	return HttpResponse("Esta es la respuesta index")

def index(request): #genera la llamada a la pagina
	return HttpResponse("Esta es la respuesta index")#respuesat del servidor a la pagina


def listado(request):
	contexto = {
		'productos': producto.objects.all(),'categorias': categoria.objects.all()
	}
	return render(request, 'productos/listado.html',contexto)


def categorias(request):
	contexto = {
		'categorias': categoria.objects.all()
	}
	return render(request, 'productos/listadoCategorias.html',contexto)
	#return HttpResponse("Esta es la respuesta cate")



	return render(request, 'productos/listado.html',contexto)
	#return HttpResponse("Esta es la respuesta listado")
def agregarProducto(request):
	if request.method == 'POST':
		form=ProductoForm(request.POST) #verificar si el formulario fue mandado el POST
		if form.is_valid(): #verifciar si el formulario en valido
			form.save() #guarda el formulario
		return redirect('listado') #redireciona a otra pagina
	else:
		form = ProductoForm() #crearemos objeto forms que importamos de nuestro form


	return render(request,'productos/formularioProducto.html')


def agregarCategoria(request):
	if request.method == 'POST':
		form=CategoriaForm(request.POST) #verificar si el formulario fue mandado el POST
		if form.is_valid(): #verifciar si el formulario en valido
			form.save() #guarda el formulario
		return redirect('listadoCategorias') #redireciona a otra pagina
	else:
		form = CategoriaForm() #crearemos objeto forms que importamos de nuestro form


	return render(request,'productos/formularioCategorias.html',{'form': form})





def editarProducto(request,idProducto):

	instance = get_object_or_404(producto, id=idProducto)
	form = ProductoForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('listado')

	return render(request, 'productos/editarProducto.html', {'form': form})


def eliminarProducto(request,idProducto):
	Producto=producto.objects.get(id=idProducto)
	Producto.delete()
	return redirect('listado')



def editarCategoria(request,idCategoria):

	instance = get_object_or_404(categoria, id=idCategoria)
	form = CategoriaForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('listadoCategorias')

	return render(request, 'productos/editarCategorias.html', {'form': form})


def eliminarCategoria(request,idCategoria):
	Categoria=categoria.objects.get(id=idCategoria)
	Categoria.delete()
	return redirect('listadoCategorias')


def venta(request):
	contexto = {
		'productos': producto.objects.exclude(numeroExistencias=0),'categorias': categoria.objects.all()
	}
	return render(request, 'productos/venta.html',contexto)


def agregarCarrito(request,idProducto):

	items=request.session.get('ids')
	if  items== None:
		items=[idProducto] #en otro caso intentar guardar todos los artributos del objeto desde el principio con .objects.get(id=idCategoria) por ejemplo
	else:
		items.append(idProducto)

	request.session['ids']=items
	return redirect('venta')




def verCarrito(request):
	items=request.session.get('ids')
	if  items== None:
	    return HttpResponse("El carrito esta vacio")
	"""contextoD=0
	for x in range(0,len(items)):
		contextoD +=(producto.objects.filter(id=items[x]))"""
	contexto = {
		'productos': producto.objects.filter(id__in=items)
	}
	#index=Counter(items)
	total=0
	#total=(producto.objects.filter(id__in=items).values('costo'))
	total=(producto.objects.filter(id__in=items).aggregate(Sum('costo')))
	contexto['total']=total
	#request.session.pop('ids')



	return render(request, 'productos/verCarrito.html',contexto)#producto.objects.filter(id=request.session.get('ids')[0])
	#return HttpResponse()



def confirmar(request):
	items=request.session.get('ids')
	#NumeroExistencias
	contexto=  producto.objects.filter(id__in=items)
	total=0
	for x in range(0,len(contexto)):
		contexto[x].numeroExistencias=contexto[x].numeroExistencias-1
		contexto[x].save()

	request.session.pop('ids')

	return redirect('venta')

