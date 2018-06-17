from django.conf.urls import url
from Mascota.views import MascotaList, MascotaFoto, MascotaEdit, MascotaAdmin, MascotaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^create', login_required(MascotaFoto), name='mascotacreate'),
    url(r'^listar', MascotaList.as_view(), name='mascotalist'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaEdit.as_view()), name='mascotaedit'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascotadelete'),
    url(r'^editar/$', login_required(MascotaAdmin.as_view()), name='mascotaadmin'),
]
