from django.db import models
from django import forms

# Create your models here.

##class Genero(models.Model):
#    idGenero = models.IntegerField(primary_key=True,db_column='idGenero')
#    idGenero = models.CharField(max_length=100,db_column='tipoGenero')
 #   class Meta:
#        db_table='Genero'
#
#class Alumno(models.Model):
#    idAlumnos = models.IntegerField(primary_key=True,db_column='idAlumno')
#    nameAlumno = models.CharField(max_length=100,db_column='nameAlumno')
#    fk_genero = models.ForeignKey(Genero,default=1,on_delete=models.CASCADE,db_column='fk_genero')
#    class Meta:
 #       db_table='Alumnos'

#class Alumno_has_Genero(models.Model):
#    fk_Alumo = models.ForeignKey(Alumno,default=1,on_delete=models.CASCADE,db_column='fk_alumno')
#    fk_genero = models.ForeignKey(Genero,default=1,on_delete=models.CASCADE,db_column='fk_genero')
#    class Meta:
#        db_table='alumno_has_genero'

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, db_column="idusu")
    nombreu = models.CharField(max_length=100, db_column="nombre")
    apellidou = models.CharField(max_length=100,db_column="apellido")
    correou = models.CharField(max_length=100, db_column="correo", unique=True)
    contraseñau = models.CharField(max_length=255,db_column="contraseña")
    class Meta:
        db_table="Usuario"


class Encuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True, db_column="idrespuesta")
    colore = models.CharField(max_length=100, db_column="color")
    frecuenciacome = models.CharField(max_length=100, db_column="frecuenciacom")
    alquiladoañoe = models.CharField(max_length=100,db_column='alquilado')
    frecuenciaalquie = models.CharField(max_length=100,db_column="frecuenciaalqui")
    factorese = models.CharField(max_length=100,db_column="factores")
    metodopagoe = models.CharField(max_length=100,db_column="metodopag")
    malexpe = models.CharField(max_length=100,db_column="malexperiencia")
    dispositivoe = models.CharField(max_length=100,db_column="dispositivo")
    recibirofe = models.CharField(max_length=100,db_column="recibiof")
    asistenciae = models.CharField(max_length=100,db_column="asistencia")
    class Meta:
        db_table="respuesta"
        




