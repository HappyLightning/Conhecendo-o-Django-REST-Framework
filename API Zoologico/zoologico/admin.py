from django.contrib import admin
from zoologico.models import Animal, Zoologico, Cativar


class Animais(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nome_cientifico', 'classe', 'familia', 'peso', 'caracteristica')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'nome_cientifico', 'classe', 'familia', 'peso')


admin.site.register(Animal, Animais)


class Zoologicos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'numero_de_animais')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome', 'endereco')


admin.site.register(Zoologico, Zoologicos)


class Cativos(admin.ModelAdmin):
    list_display = ('id', 'animal', 'zoo', 'periodo')
    list_display_links = ('id',)


admin.site.register(Cativar, Cativos)
