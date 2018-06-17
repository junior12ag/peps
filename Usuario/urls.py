from django.conf.urls import url
from Usuario.views import RegistroUsuario



urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name='registro'),
    


]
