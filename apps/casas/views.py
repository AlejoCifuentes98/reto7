from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .models import Propietario, Casa


def inicio_view(request):
    casas = Casa.objects.filter()
    return render(request,'casas/inicio.html', locals())


def registro_view(request):
    if request.method == 'POST':
        form_propietario_registrar = propietario_agregar_form(request.POST)
        form_casa_registrar = casa_agregar_form(request.POST, request.FILES)
        if form_propietario_registrar.isvalid() and form_casa_registrar.isvalid():
            p= form_propietario_registrar.save()
            c =form_casa_registrar.save(commit=False)
            c.propietario = p
            c.save()
    return render(request,'casas/registro.html', locals())    

def login_view(request):
    usu =""
    cla= ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        usuario = authenticate(username=usu, password=cla)
        if usuario is not None and usuario.is_active:
            login(request, usuario)
            return redirect('/')
        else:
            msj = 'usuario o clave incorrectos'    
    return render(request,'casas/login.html', locals())

def logout_view(request):
    logout(request)
    return redirect('/login/')

def casa_registrar_view(request):
    if request.method == 'POST':
        form_casa_registrar= casa_registrar_form(request.POST)
        if form_casa_registrar.isvalid():
            form_casa_registrar.save()
        else: 
            msj = 'Ocurrio un error, por favor intente nuevamente'    
    else:
        form_casa_registrar= casa_registrar_form()        
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
    propietarios = Propietario.objects.filter()
    return render(request,'casas/propietarios.html', locals())

def propietario_registrar_view(request):
    if request.method == 'POST':
        form_propietario_registrar = propietario_registar_form(request.POST)
        if form_propietario_registrar.isvalid():
            form_propietario_registrar.save()
    else:
        form_propietario_registrar = propietario_registar_form()        
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
