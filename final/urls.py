"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.productos.views import index,listado,agregarProducto,agregarCategoria,categorias,editarProducto,eliminarProducto,\
editarCategoria,eliminarCategoria,venta,agregarCarrito,verCarrito,confirmar
#from django.views.generic.base import TemplateView
from django.views.generic import TemplateView
#from django.views.generic.simple import direct_to_template

app_name='productos'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/',direct_to_template, {"template": "index.html"}),
    path('', TemplateView.as_view(template_name='productos/home.html'),name='home'),
    path('listado/',listado,name="listado"),
    path('listadoCategorias/',categorias,name="listadoCategorias"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('agregarCategoria/',agregarCategoria,name="agregarCategoria"),
    path('editarProducto/<idProducto>',editarProducto,name="editarProducto"),
    path('eliminarProducto/<idProducto>',eliminarProducto,name="eliminarProducto"),
    path('editarCategoria/<idCategoria>',editarCategoria,name="editarCategoria"),
    path('eliminarCategoria/<idCategoria>',eliminarCategoria,name="eliminarCategoria"),
    path('venta/',venta,name="venta"),
    path('agregarCarrito/<idProducto>',agregarCarrito,name="agregarCarrito"),
    path('verCarrito/',verCarrito,name="verCarrito"),
    path('confirmar/',confirmar,name="confirmar"),



    

]
