from django.contrib import admin
from.models import HoraMedica,Medico,EspecialidadMedica,CentroMedico,HoraAtencion

# Register your models here.

admin.site.register([HoraMedica])
admin.site.register([Medico])
admin.site.register([EspecialidadMedica])
admin.site.register([CentroMedico])
admin.site.register([HoraAtencion])