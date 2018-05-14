from __future__ import unicode_literals
from django.db.models import Count
from django.db import models
from django.core.validators import ValidationError, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class sala_manager(models.Manager):
    def obtiene_disponible(self):
    	s = self.filter(estado = "E").first()
    	if (s == None):
    		s = self.create()
    	return s
# Create your models here.
class sala(models.Model):
	estados = (
		("J", u"Jugando"),
		("E", u"Esperando jugadores"),
		("O", u"Ordenando jugadores"),
		("D", u"Desactivado")
		)
	estado = models.CharField(max_length=1, default="E", choices=estados)
	objects = sala_manager()
	cuenta = models.IntegerField(
			default=7,
			validators=[
				MaxValueValidator(30),
				MinValueValidator(1)
			]
		)
	def __unicode__(self):
		return u"%s - %s"%(self.id,self.estado)
	def clean(self):
		if(len(self.__class__.objects.filter(estado="E")) != 0 and not self.id):
			raise ValidationError({"estado":_(u'Existe una sala en espera de juegadores.')})
		if (self.estado == "E" and self.id):
			raise ValidationError({"estado":_(u'No puede cambiar la sala a "Esperando jugadores".')})
	def save(self, *args, **kwargs):
		if(len(self.__class__.objects.filter(estado="E")) != 0 and not self.id):
			raise ValidationError({"estado":_(u'Existe una sala en espera de juegadores.')})
		if(self.estado == "E" and self.id and self.cuenta < 5):
			raise ValidationError({"estado":_(u'No puede cambiar la sala a "Esperando jugadores".')})
		if(self.cuenta <= 5 and self.cuenta > 0):
			self.estado = "O"
		if(self.cuenta == 0):
			self.estado = "J"
		super(sala, self).save(*args, **kwargs)
		####################################
		######### Aqui va el background task
		####################################

class jugador(models.Model):
	estados = ((True, u"Vivo"),(False, u"Muerto"))
	sala = models.ForeignKey(sala)
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(choices=estados, default=True)
	def __unicode__(self):
		return u"%s - %s"%(self.id,self.nombre)
	def save(self, *args, **kwargs):
		s = sala.objects.obtiene_disponible()
		self.sala = s
		super(jugador, self).save(*args, **kwargs)