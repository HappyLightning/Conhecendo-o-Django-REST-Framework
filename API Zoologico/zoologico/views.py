from rest_framework import viewsets
from zoologico.models import Animal, Zoologico
from zoologico.serializer import AnimalSerializer, ZoologicoSerializer


class AnimaisViewSet(viewsets.ModelViewSet):
	""" Todos os animais """
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer


class ZoologicosViewSet(viewsets.ModelViewSet):
	""" Todos os zoológicos """
	queryset = Zoologico.objects.all()
	serializer_class = ZoologicoSerializer
	