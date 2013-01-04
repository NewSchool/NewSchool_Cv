from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.ForeignKey(User, unique=True)
    direccion = models.CharField(max_length=250, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
		verbose_name_plural = "perfiles"

class institucion(models.Model):
	nombre		= models.CharField(max_length=200)
	dane		= models.CharField(max_length=200)
	email		= models.EmailField()
	telefono	= models.CharField(max_length=200)
	tema		= models.CharField(max_length=200)
	escudo		= models.ImageField(upload_to="static/uploads")


	status		= models.BooleanField(default=True)

	def __unicode__(self):
		return (self.nombre)


	class Meta:
		verbose_name_plural = "Instituciones"

class jornada(models.Model):
	nombre		= models.CharField(max_length=200)
	
	def __unicode__(self):
		return (self.nombre)


class grado(models.Model):
	nombre		= models.CharField(max_length=200)
	
	def __unicode__(self):
		return (self.nombre)

class nivel(models.Model):
	nombre		= models.CharField(max_length=200)
	
	def __unicode__(self):
		return (self.nombre)

	class Meta:
		verbose_name_plural = "Niveles"

