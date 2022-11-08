from django.contrib import admin
from django.urls import path, include
from zoologico.views import AnimaisViewSet, ZoologicosViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('animais', AnimaisViewSet, basename='Animais')
router.register('zoologicos', ZoologicosViewSet, basename='Zoologicos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
