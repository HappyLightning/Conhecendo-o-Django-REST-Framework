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


# Classe para relacionamento entre os dois modelos acima.
class Cativar(models.Model):
    periodo_exibicao = (('M', 'matutino'), ('V', 'vespertino'), ('N', 'noturno'))  # Lista de tuplas das possíveis escolhas.

    # Referências da Chave Estrangeira de cada tabela no banco.
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)  # 'on_delete=models.CASCADE' para não referenciar animais deletados.
    zoo = models.ForeignKey(Zoologico, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=periodo_exibicao, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Cativos'