from django.db import models

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

