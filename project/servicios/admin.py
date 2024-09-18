from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'talle', 'stock',)
    search_fields = ('nombre', 'precio', 'talle', 'stock',)
    ordering = ('precio',)

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'celular', 'cuit', 'domicilio',)
    search_fields = ('nombre', 'apellido',)
    ordering = ('apellido', 'nombre',)

@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'fecha_solicitud', 'fecha_entrega', 'estado',)
    search_fields = ('cliente', 'estado', 'producto',)