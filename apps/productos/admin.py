from django.contrib import admin
from apps.productos.models import producto
from apps.productos.models import categoria

# Register your models here.
admin.site.register(producto)
admin.site.register(categoria)