# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=25, blank=True, null=True)
    apellido = models.CharField(max_length=25, blank=True, null=True)
    nro_contacto = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    dni = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class DetalleProducto(models.Model):
    cantidad_necesaria = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    insumo = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='insumo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_producto'


class DetalleVenta(models.Model):
    cantidad_producto = models.IntegerField(blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class EstadoVenta(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_venta'


class Insumo(models.Model):
    nombre = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'insumo'


class Producto(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    precio_unitario = models.IntegerField(blank=True, null=True)
    detalle_producto = models.ForeignKey(DetalleProducto, models.DO_NOTHING, db_column='detalle_producto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Sucursal(models.Model):
    direccion = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Venta(models.Model):
    fecha_hora = models.DateTimeField(blank=True, null=True)
    sucursal = models.IntegerField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    detalle_venta = models.ForeignKey(DetalleVenta, models.DO_NOTHING, db_column='detalle_venta', blank=True, null=True)
    estado_venta = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='estado_venta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
