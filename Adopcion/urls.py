from django.conf.urls import url
from Adopcion.views import SolicitudAdopcionCreate, SolicitudList,Solicitud, SolicitudVer, SolicitudTest, SolicitudUpdate, Complete
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings
urlpatterns = [
    url(r'^solicitud/(?P<pk>\d+)/$', Solicitud, name='solicitud'),
    url(r'^listar/', login_required(SolicitudList.as_view()), name='solicitudlist'),
    url(r'^estado/(?P<pk>\d+)/$', login_required(SolicitudUpdate), name='estado'),
    url(r'^compelete', Complete, name='complete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
