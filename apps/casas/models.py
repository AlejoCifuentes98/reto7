from django.db import models


class Propietario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    identificacion = models.IntegerField()
    telefono = models.IntegerField()
    correo = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos + ' ' + str(self.identificacion)

estados= (
    ('En reconstruccion', 'En reconstruccion'),
    ('Por terminar', 'Por terminar'),
    ('Terminada', 'Terminada'),

)
class Casa(models.Model):
    direccion = models.CharField(max_length=60)        
    barrio = models.CharField(max_length=30)
    estado = models.CharField(max_length= 30,choices=estados, default='En reconstruccion')
    imagen_inicial = models.ImageField(upload_to='imagen_inicial')
    imagen_final = models.ImageField(upload_to='imagen_final', null=True, blank=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.id) + ' ' + self.direccion + ' ' + self.estado