from rest_framework import serializers
from zoologico.models import Animal, Zoologico, Cativar


class AnimalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Animal
		fields = ['id', 'nome', 'nome_cientifico', 'classe', 'familia', 'peso', 'caracteristica']


class ZoologicoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Zoologico
		fields = '__all__'  # Mesma coisa que criar uma lista como acima.


class CativarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cativar
		exclude = []


class ListaCativeirosAnimalSerializer(serializers.ModelSerializer):
	animal = serializers.ReadOnlyField(source='animal.nome')
	zoo = serializers.ReadOnlyField(source='zoo.nome')


	class Meta:
		model = Cativar
		fields = ['animal', 'zoo', 'periodo']


class ListaAnimaisCativosnoZoologico(serializers.ModelSerializer):
	animal_nome = serializers.ReadOnlyField(source='animal.nome')
	class Meta:
		model = Cativar
		fields = ['animal_nome']
