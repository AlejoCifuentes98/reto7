from django.urls import path
from .views import inicio_view, registro_view, login_view, logout_view, casa_registrar_view, casa_editar_view, casa_eliminar_view, propietarios_view, propietario_registrar_view, propietario_editar_view, propietario_eliminar_view

urlpatterns = [
    path('', inicio_view, name='inicio'),

    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('casa_registrar/', casa_registrar_view, name='casa_registrar'),
    path('casa_editar/<int:id_casa>/', casa_editar_view, name='casa_editar'),
    path('casa_eliminar/<int:id_casa>/', casa_eliminar_view, name='casa_eliminar'),
    
    path('propietarios/', propietarios_view, name='propietarios'),
    path('propietario_registrar/', propietario_registrar_view, name='propietario_registrar'),
    path('propietario_editar/<int:id_propietario>/', propietario_editar_view, name='propietario_editar'),
    path('propietario_eliminar/<int:id_propietario>/', propietario_eliminar_view, name='propietario_eliminar'),
    
]