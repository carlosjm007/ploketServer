# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
import TEST.models as TestModels
import TEST.serializers as TestSerial

# Create your views here.
class JugadorViewSet(viewsets.ModelViewSet):
	queryset = TestModels.jugador.objects.none()
	serializer_class = TestSerial.SerialJugador

class UserViewSet(viewsets.ViewSet):
	"""
	Example empty viewset demonstrating the standard
	actions that will be handled by a router class.

	If you're using format suffixes, make sure to also include
	the `format=None` keyword argument for each action.
	"""
	queryset = TestModels.jugador.objects.none()
	serializer_class = TestSerial.SerialJugador

	def list(self, request):
		pass

	def create(self, request):
		pass

	def retrieve(self, request, pk=None):
		pass

	def update(self, request, pk=None):
		print "aja - %s"%(pk)
		jugador = TestModels.jugador.objects.get(id=pk)
		jugador.estado = False
		jugador.save()
		serializer = self.serializer_class(jugador, many=False)
		return Response(serializer.data)

	def partial_update(self, request, pk=None):
		pass

	def destroy(self, request, pk=None):
		pass