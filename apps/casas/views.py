from django.shortcuts import render
from .models import Propietario, Casa


def inicio_view(request):
    casas = Casa.objects.filter()
    return render(request,'casas/inicio.html', locals())


def registro_view(request):

    return render(request,'casas/registro.html', locals())    

def login_view(request):
    return render(request,'casas/login.html', locals())

def logout_view(request):
    return render(request,'casas/logout.html', locals())

def casa_registrar_view(request):
    return render(request,'casas/casa_registrar.html', locals)

def casa_editar_view(request,id_casa):
    return render(request,'casas/casa_editar.html', locals())

def casa_eliminar_view(request):
    return render(request,'casas/casa_eliminar', locals())

def propietarios_view(request):
    return render(request,'casas/propietarios.html', locals())

def propietario_registrar_view(request):
    return render(request,'casas/propietario_registrar.html', locals())

def propietario_editar_view(request):
    return render(request,'casas/propietario_editar.html', locals())

def propietario_eliminar_view(request):
    return render(request,'casas/propietario_eliminar_view.html', locals())    
