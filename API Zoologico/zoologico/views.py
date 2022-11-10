from rest_framework import viewsets, generics
from zoologico.models import Animal, Zoologico, Cativar
from zoologico.serializer import AnimalSerializer, ZoologicoSerializer, CativarSerializer, ListaCativeirosAnimalSerializer, ListaAnimaisCativosnoZoologico
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AnimaisViewSet(viewsets.ModelViewSet):
	""" Todos os animais """
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class ZoologicosViewSet(viewsets.ModelViewSet):
	""" Todos os zoológicos """
	queryset = Zoologico.objects.all()
	serializer_class = ZoologicoSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class CativarViewSet(viewsets.ModelViewSet):
	"""Todos os cativos... coitados"""
	queryset = Cativar.objects.all()
	serializer_class = CativarSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class ListaCativeirosAnimal(generics.ListAPIView):
	"""Listando os animais cativos em... coitados"""
	def get_queryset(self):
		queryset = Cativar.objects.filter(animal_id=self.kwargs['pk'])
		return queryset
	serializer_class = ListaCativeirosAnimalSerializer


class ListaAnimaisZoologico(generics.ListAPIView):
	"""Listando os animais de um Zoológico"""
	def get_queryset(self):
		queryset = Cativar.objects.filter(zoo_id = self.kwargs['pk'])
		return queryset
	serializer_class = ListaAnimaisCativosnoZoologico



