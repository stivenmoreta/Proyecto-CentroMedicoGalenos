# Generated by Django 3.2.9 on 2021-11-22 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentroMedico',
            fields=[
                ('idCentroMedico', models.AutoField(primary_key=True, serialize=False, verbose_name='Id centro medico')),
                ('direccionCentroMedico', models.CharField(blank=True, max_length=80, null=True, verbose_name='Direccion centro medico')),
            ],
        ),
        migrations.CreateModel(
            name='EspecialidadMedica',
            fields=[
                ('idEspecialidadMedica', models.AutoField(primary_key=True, serialize=False, verbose_name='Id especialidad medica')),
                ('nombreEspecialidadMedica', models.CharField(max_length=80, verbose_name='Especialidad Medica')),
            ],
        ),
        migrations.CreateModel(
            name='HoraAtencion',
            fields=[
                ('idHora', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la hora')),
                ('hora', models.CharField(blank=True, max_length=5, null=True, verbose_name='Hora de Atencion')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('idMedico', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Medico')),
                ('nombreMedico', models.CharField(max_length=80, verbose_name='Nombre Medico')),
            ],
        ),
        migrations.CreateModel(
            name='HoraMedica',
            fields=[
                ('idHoraMedica', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la hora medica')),
                ('fechaAtencion', models.DateField(verbose_name='Fecha de atencion')),
                ('estadoHora', models.BooleanField(verbose_name='Hora disponible')),
                ('centroMedico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.centromedico')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.especialidadmedica')),
                ('horaAtencion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.horaatencion')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.medico')),
            ],
        ),
    ]
