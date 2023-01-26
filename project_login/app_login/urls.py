from django.urls import path
from.import views

urlpatterns = [
    path('', views.main, name='main'),
    path('inicio/', views.inicio, name='inicio'),
    path('hisoria/', views.historia, name='historia'),
    path('automatizacion/', views.automatizacion, name='automatizacion'),
    path('inteligencia/', views.inteligencia, name='inteligencia'),
    path('nuevas_tec/', views.nuevas_tec, name='nuevas_tec'),
    path('contac/', views.contac, name='contac'),
    path('salir/', views.salir, name='salir'),
]
