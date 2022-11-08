from rest_framework import serializers
from zoologico.models import Animal, Zoologico


class AnimalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Animal
		fields = ['id', 'nome', 'nome_cientifico', 'classe', 'familia', 'peso', 'caracteristica']


class ZoologicoSerializer(serializers.ModelSerializer):
	model = Zoologico
	fields = '__all__'  # Mesma coisa que criar uma lista como acima.