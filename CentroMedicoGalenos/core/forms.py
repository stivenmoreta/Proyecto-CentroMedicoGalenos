from django.forms import ModelForm, DateInput

from .models import HoraMedica


class HoraMedicaForm(ModelForm):
    class Meta:
        model = HoraMedica
        fields = ['especialidad','centroMedico','medico','fechaAtencion','horaAtencion']
        widgets = {'fechaAtencion': DateInput(attrs={'type':'date'})}

class EstadoHoraMedicaForm(ModelForm):
    class Meta:
        model = HoraMedica
        fields = ['estadoHora']
        labels  = {
        'estadoHora':'Anular', 
        }
        
