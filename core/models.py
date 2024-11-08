# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    nombre_pila = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'administrador'


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_veterinario = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='id_veterinario')
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    id_dueno = models.ForeignKey('Dueno', models.DO_NOTHING, db_column='id_dueno')
    seguimiento = models.CharField(max_length=200, blank=True, null=True)
    costo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField()
    diagnostico = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cita'


from django.db import models

class Detalle(models.Model):
    id_cita = models.OneToOneField(
        'Cita', 
        models.DO_NOTHING, 
        db_column='id_cita', 
        primary_key=True
    )
    id_veterinario = models.BigIntegerField(unique=True) 
    motivo = models.CharField(max_length=200, blank=True, null=True)
    tratamiento = models.CharField(max_length=200, blank=True, null=True)
    calificacion = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle'
        unique_together = (('id_cita', 'id_veterinario'),)



class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    nombre_pila = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dueno'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_item = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_item', blank=True, null=True)
    id_cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='id_cita', blank=True, null=True)
    id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='id_dueno')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='id_dueno')
    nombre = models.CharField(max_length=50, blank=True, null=True)
    especie = models.CharField(max_length=50, blank=True, null=True)
    raza = models.CharField(max_length=30, blank=True, null=True)
    edad_num = models.FloatField(blank=True, null=True)
    unidad_tiempo = models.CharField(max_length=10, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    diagnostico = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class Producto(models.Model):
    id_item = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    cantidad = models.FloatField(blank=True, null=True)
    existencia = models.FloatField(blank=True, null=True)
    id_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_administrador')

    class Meta:
        managed = False
        db_table = 'producto'


class Usuario(models.Model):
    usuario_id = models.BigIntegerField(primary_key=True)
    rol = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=100)
    nombre_usuario = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'


from django.db import models

class Valoracion(models.Model):
    id_valoracion = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey(Detalle, models.DO_NOTHING, db_column='id_cita')
    id_veterinario = models.OneToOneField(
        Detalle,
        models.DO_NOTHING,
        db_column='id_veterinario',
        to_field='id_veterinario',
        related_name='valoracion_id_veterinario_set', unique=True
    )
    calificacion = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valoracion'


class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)
    nombre_pila = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    especialidad = models.CharField(max_length=50, blank=True, null=True)
    horario_inicio = models.DateTimeField(blank=True, null=True)
    horario_fin = models.DateTimeField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veterinario'