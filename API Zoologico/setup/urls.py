from django.contrib import admin
from django.urls import path, include
from zoologico.views import AnimaisViewSet, ZoologicosViewSet, CativarViewSet, ListaCativeirosAnimal, ListaAnimaisZoologico
from rest_framework import routers


router = routers.DefaultRouter()
router.register('animais', AnimaisViewSet, basename='Animais')
router.register('zoologicos', ZoologicosViewSet, basename='Zoologicos')
router.register('cativos', CativarViewSet, basename='Cativar')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('animais/<int:pk>/cativos', ListaCativeirosAnimal.as_view()),
    path('zoologicos/<int:pk>/cativos', ListaAnimaisZoologico.as_view()),  # O inverso.
]
