from django.urls import path;
from .views import index,listar_hora_medica,agendar_hora_medica,anular_hora_medica,eliminar_hora;

urlpatterns = [
    path('', index, name="index"),
    path('horasPaciente', listar_hora_medica, name="horasPaciente"),
    path('registrarHoraMedica/<action>/<id>', agendar_hora_medica, name="registrarHoraMedica"),
    path('anularHora/<id>', anular_hora_medica, name="anularHora"),
    path('eliminarHora/<id>', eliminar_hora, name="eliminarHora"),

]