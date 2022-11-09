from rest_framework import viewsets
from zoologico.models import Animal, Zoologico, Cativar
from zoologico.serializer import AnimalSerializer, ZoologicoSerializer, CativarSerializer


class AnimaisViewSet(viewsets.ModelViewSet):
	""" Todos os animais """
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer


class ZoologicosViewSet(viewsets.ModelViewSet):
	""" Todos os zoológicos """
	queryset = Zoologico.objects.all()
	serializer_class = ZoologicoSerializer


class CativarViewSet(viewsets.ModelViewSet):
	"""Todos os cativos... coitados"""
	queryset = Cativar.objects.all()
	serializer_class = CativarSerializer