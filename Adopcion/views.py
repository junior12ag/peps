from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from Adopcion.models import SolicitudAdopcion
from Adopcion.forms import SolicitudAdopcionForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from Mascota.models import Mascota
from Mascota.forms import MascotaForm
import time


# Create your views here.

class SolicitudAdopcionCreate(CreateView):
    model = SolicitudAdopcion
    form_class = SolicitudAdopcionForm
    template_name = 'adopcion/solicitud.html'
    success_url = reverse_lazy('adopcion:complete')

class SolicitudList(ListView):
    model = SolicitudAdopcion
    template_name = 'adopcion/solicitudlist.html'


def Solicitud(request, pk):
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('adopcion:complete')
    else:
        form = SolicitudAdopcionForm(initial={'mascota':pk, 'fecha': time.strftime("%Y-%m-%d")})
        #form -SolicitudAdopcionForm['mascota': pk]
    return render(request, 'adopcion/solicitud.html', {'form':form})

class SolicitudVer(UpdateView):
    model = SolicitudAdopcion
    form_class = SolicitudAdopcionForm
    template_name = 'adopcion/solicitudaceptar.html'
    #pk = SolicitudAdopcionForm.Meta.fields['mascota'].value
    #mascota = Mascota.objects.get(pk=pk)
    #mascota.estado =True
    #smascota.save()
    success_url = reverse_lazy('adopcion:solicitudlist')

class SolicitudTest(UpdateView):
    model = SolicitudAdopcion
    fields = [
        'nombre',
        'apellidos',
        'email',
        'sexo',
        'edad',
        'identificacion',
        'direccion',
        'razon',
        'fecha',
        'mascota',
        'telefono',
        'ocupacion',
        'estado'

    ]
    template_name = 'adopcion/solicitudaceptar.html'
    #pk = model.mascota.get_value()


    success_url =reverse_lazy('adopcion:solicitudlist')


def SolicitudUpdate(request, pk):
    instance = SolicitudAdopcion.objects.get(id=pk)
    if request.method == 'GET':
        form = SolicitudAdopcionForm(instance=instance)

    else:
        form = SolicitudAdopcionForm(request.POST, instance=instance)
        if form.is_valid():

            mascota = Mascota.objects.get(pk=instance.mascota.pk)
            mascota.estado = True
            mascota.save()
            form.save()
        return redirect('adopcion:solicitudlist')
    return render(request, 'adopcion/solicitudaceptar.html', {'form': form} )


def Complete(request):
    return render(request, 'adopcion/solicitudcomplete.html')
