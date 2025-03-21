from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('tiposPropietarios/', views.listar_tipos_propietarios, name='listar_tiposPropietarios'),
    path('crearTipoPropietario/', views.crearTipoPropietario, name='crearTipoPropietario'),
    path('editar/tipoPropietario<int:id>', views.editarTipoPropietario, name='editarTipoPropietario'),
    path('borrar/tipoPropietario<int:id>', views.borrarTipoPropietario, name='borrarTipoPropietario'),

    path('propietarios/', views.listar_propietarios, name='listar_propietarios'),
    path('crearPropietario/', views.crearPropietario, name='crearPropietario'),
    path('editar/propietario<int:id>', views.editarPropietario, name='editarPropietario'),
    path('borrar/propietario<int:id>', views.borrarPropietario, name='borrarPropietario'),

    path('departamentos/', views.listar_departamentos, name='listar_departamentos'),
    path('crearDepto/', views.crearDepto, name='crearDepto'), 
    path('editar/departametos<int:id>', views.editarDepto, name='editarDepto'),
    path('borrar/departamento<int:id>/', views.borrarDepto, name='borrarDepto'),

    path('ciudades/', views.listar_ciudades, name='listar_ciudades'),
    path('crearCiudad/', views.crearCiudad, name='crearCiudad'),
    path('editar/ciudades<int:id>', views.editarCiudad, name='editarCiudad'),
    path('borrar/ciudad<int:id>', views.borrarCiudad, name='borrarCiudad'),

    path('distritos/', views.listar_distritos, name='listar_distritos'),
    path('crearDistrito/', views.crearDistrito, name='crearDistrito'),
    path('editar/distritos<int:id>', views.editarDistrito, name='editarDistrito'),
    path('borrar/distrito<int:id>', views.borrarDistrito, name='borrarDistrito'),

    path('tiposPropiedades/', views.listar_tipos_propiedades, name='listar_tipos_propiedades'),
    path('crearTipoPropiedad/', views.crearTipoPropiedad, name='crearTipoPropiedad'),
    path('editar/tipoPropiedad<int:id>', views.editarTipoPropiedad, name='editarTipoPropiedad'),
    path('borrar/tipoPropiedad<int:id>', views.borrarTipoPropiedad, name='borrarTipoPropiedad'),

    path('transacciones/', views.listar_transacciones, name='listar_transacciones'), 
    path('crearTransaccion/', views.crearTransaccion, name='crearTransaccion'),
    path('editar/transaccion<int:id>', views.editarTransaccion, name='editarTransaccion'),
    path('borrar/transaccion<int:id>', views.borrarTransaccion, name='borrarTransaccion'),

    path('inmuebles/', views.listarProperty, name='listar_inmuebles'),
    path('crearInmueble/', views.crearProperty, name='crearInmueble'),
    path('editar/inmueble<int:id>', views.editarProperty, name='editarInmueble'),
    path('borrar/inmueble<int:id>', views.borrarProperty, name='borrarInmueble'),

    path('nosotros/', views.nosotros, name='nosotros'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
