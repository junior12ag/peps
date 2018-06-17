from Mascota.models import Mascota
from django import forms


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'edad',
            'raza',
            'sexo',
            'foto',
            'video',
            'vacuna'


        ]

        labels ={
            'nombre': 'Nombre',
            'edad': 'Edad',
            'raza': 'Raza',
            'sexo': 'Sexo',
            'foto': 'Foto',
            'video': 'Video',
            'vacuna': 'Vacunas',
            

        }

        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'raza':forms.TextInput(attrs={'class': 'form-control'}) ,
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.TextInput(attrs={'class': 'form-control'}),


        }
