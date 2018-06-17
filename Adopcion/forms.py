from django import forms
from Adopcion.models import SolicitudAdopcion

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
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

        labels = {
                'nombre': 'Nombre',
                'apellidos': 'Apellidos',
                'email': 'Email',
                'sexo': 'Sexo',
                'edad': 'Edad',
                'identificacion':'Identificacion' ,
                'direccion': 'Direccion' ,
                'razon': 'Razones',
                'fecha':'Fecha' ,
                'mascota': 'Numero Mascota',
                'telefono': 'Telefono',
                'ocupacion': 'Ocupacion',
                'estado': 'Estado',

        }

        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion':forms.Textarea(attrs={'class': 'form-control'}),
            'razon': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'from-control', 'readonly': 'readonly'}),
            'mascota': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'ocupacion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.NullBooleanSelect(),


        }
