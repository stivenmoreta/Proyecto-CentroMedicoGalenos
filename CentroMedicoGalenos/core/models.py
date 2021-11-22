from django.db import models

# Create your models here.

class CentroMedico(models.Model):
    idCentroMedico = models.AutoField(primary_key=True, verbose_name="Id centro medico")
    direccionCentroMedico = models.CharField(max_length=80, blank=True, null=True, verbose_name="Direccion centro medico")

    def __str__(self):
        return self.direccionCentroMedico

class EspecialidadMedica(models.Model):
    idEspecialidadMedica = models.AutoField(primary_key=True, verbose_name="Id especialidad medica")
    nombreEspecialidadMedica = models.CharField(max_length=80, blank=False, null=False, verbose_name="Especialidad Medica")

    def __str__(self):
        return self.nombreEspecialidadMedica

class Medico(models.Model):
    idMedico = models.AutoField(primary_key=True, verbose_name="Id Medico")
    nombreMedico = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre Medico")

    def __str__(self):
        return self.nombreMedico

class HoraAtencion(models.Model):
    idHora = models.AutoField(primary_key=True, verbose_name="Id de la hora")
    hora = models.CharField(max_length=5, blank=True, null=True, verbose_name="Hora de Atencion")

    def __str__(self):
        return self.hora

        

class HoraMedica(models.Model):
    idHoraMedica = models.AutoField(primary_key=True, verbose_name="Id de la hora medica")
    fechaAtencion = models.DateField(verbose_name="Fecha de atencion")
    horaAtencion = models.ForeignKey(HoraAtencion, on_delete=models.DO_NOTHING)
    centroMedico = models.ForeignKey(CentroMedico, on_delete=models.DO_NOTHING)
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING)
    especialidad = models.ForeignKey(EspecialidadMedica, on_delete=models.DO_NOTHING)
    estadoHora = models.BooleanField(default=True, verbose_name="Hora disponible")

    def __str__(self):
        return self.idHoraMedica