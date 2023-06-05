# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
