from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from Mascota.models import Mascota
from Mascota.forms import MascotaForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def Index(request):
    return render(request, 'Index.html')

class MascotaList(ListView):
    template_name = 'mascota/mascotalist.html'
    model = Mascota

class MascotaAdmin(ListView):
    template_name = 'mascota/mascotaadmin.html'
    model = Mascota


def MascotaFoto(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mascota:mascotaadmin')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascotacreate.html', {'form':form})

class MascotaEdit(UpdateView):
    model = Mascota
    template_name = 'mascota/mascotacreate.html'
    form_class = MascotaForm
    success_url = reverse_lazy('mascota:mascotaadmin')


class MascotaDelete(DeleteView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascotadelete.html'
    success_url = reverse_lazy('mascota:mascotaadmin')
