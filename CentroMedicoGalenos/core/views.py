from django.http.request import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

#Importacion de formularios
from .forms import HoraMedicaForm,EstadoHoraMedicaForm

#Importacion de modelos
from .models import HoraAtencion, HoraMedica

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def listar_hora_medica(request):
    data = {"lista": HoraMedica.objects.all().order_by('fechaAtencion')}
    return render(request, "core/horasPaciente.html", data)

def anular_hora_medica(request,id):
    horaMedica = get_object_or_404(HoraMedica, idHoraMedica=id)
    data = {'form': EstadoHoraMedicaForm(instance=horaMedica)}

    if request.method =='POST':
        formulario = EstadoHoraMedicaForm(data=request.POST, instance=horaMedica)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="horasPaciente")
    return render(request, "core/anularHora.html", data)
    
def eliminar_hora(request, id):
    horaMedica = get_object_or_404(HoraMedica, idHoraMedica=id)
    horaMedica.delete()
    return redirect(to='horasPaciente')


def agendar_hora_medica(request, action, id):
    data = {"mesg": "", "form": HoraMedicaForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = HoraMedicaForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡Hora agendada!"
                except Exception as e:
                    print(e)
                    data["mesg"] = "¡Hora no agendada!"
    return render(request, "core/registrarHoraMedica.html", data) 
