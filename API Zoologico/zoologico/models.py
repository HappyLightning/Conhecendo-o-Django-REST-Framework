from django.db import models


class Animal(models.Model):
	nome = models.CharField(max_length=30)
	nome_cientifico = models.CharField(max_length=40)
	classe = models.CharField(max_length=20)
	familia = models.CharField(max_length=20)
	peso = models.DecimalField(max_digits=6, decimal_places=3)  # Em kg.
	caracteristica = models.TextField()


	def __str__(self):
		return self.nome


	class Meta:
		verbose_name_plural = 'Animais'


class Zoologico(models.Model):
	nome = models.CharField(max_length=30)
	endereco = models.CharField(max_length=40)
	numero_de_animais = models.IntegerField()


	def __str__(self):
		return self.nome


	class Meta:
		verbose_name_plural = 'Zoologicos'