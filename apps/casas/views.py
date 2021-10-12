from django.shortcuts import redirect, render
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
    casa = Casa.objects.get(id=id_casa)
    if request.method == 'GET':
        form_casa_editar = casa_editar_form(instance=casa)
    else:
        form_casa_editar = casa_editar_form(request.POST, instance=casa)
        if form_casa_editar.isvalid():
            form_casa_editar.save()
            return redirect('/')        
    return render(request,'casas/casa_editar.html', locals())

def casa_eliminar_view(request, id_casa):
    casa = Casa.objects.get(id = id_casa)
    if request.method == 'POST':
        casa.delete()
        return redirect('/')
    return render(request,'casas/casa_eliminar', locals())

def propietarios_view(request):
    return render(request,'casas/propietarios.html', locals())

def propietario_registrar_view(request):
    return render(request,'casas/propietario_registrar.html', locals())

def propietario_editar_view(request, id_propietario):
    propietario = Propietario.objects.get(id = id_propietario)
    if request.method == 'GET':
        form_propietario_editar= propietario_editar_form(instance=propietario)
    else:
        form_propietario_editar = propietario_editar_form(request.POST, instance=propietario)
        if form_propietario_editar.isvalid():
            form_propietario_editar.save()
            return redirect('/propietarios/')    
    return render(request,'casas/propietario_editar.html', locals())

def propietario_eliminar_view(request, id_propietario):
    propietario = Propietario.objects.get(id = id_propietario)
    if request.method == 'POST':
        propietario.delete()
        return redirect('/propietarios/')
    return render(request,'casas/propietario_eliminar_view.html', locals())    
