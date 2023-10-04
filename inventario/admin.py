from django.contrib import admin

# Register your models here.

from .models import Categoria
from .models import Producto

from .models import Orden
from .models import OrdenProducto

admin.site.register(Categoria)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades", "disponible")
admin.site.register(Producto, ProductoAdmin)

admin.site.register(Orden)
admin.site.register(OrdenProducto)