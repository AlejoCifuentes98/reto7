from django.forms import forms
from .models import Propietario, Casa, User

#formulario a base del modelo para agregar un propietario
class propietario_form(models.Model):
    class Meta:
        model = Propietario #el modelo base
        fields = '__all__' #todos los campos
        exclude = [] #No excluir ningun campo

#formulario a base del modelo para agregar una casa
class casa_form(models.Model):
    class Meta:
        model = Casa #el modelo base
        fields = '__all__' #todos los campos
        exclude = ['propietario'] #excluye la llave foranea del propietario que se pondran en la vista
