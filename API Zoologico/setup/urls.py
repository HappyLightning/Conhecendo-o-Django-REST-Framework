from django.contrib import admin
from django.urls import path
from zoologico.views import animais


urlpatterns = [
    path('admin/', admin.site.urls),
    path('animais/', animais)
]
