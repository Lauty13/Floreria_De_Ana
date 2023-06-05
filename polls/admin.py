from django.contrib import admin

# Register your models here.

from Floreria.models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Sucursal)
admin.site.register(Insumo)
admin.site.register(DetalleProducto)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
admin.site.register(EstadoVenta)
admin.site.register(Venta)

