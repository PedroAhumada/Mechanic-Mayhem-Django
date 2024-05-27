from django.db import models

# Create your models here.
class Genero(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion
    
class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion
    
class Categorias(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField(default=0)
    dirrecion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    habilitado = models.BooleanField(default=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="empleados", null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
    
class SubirProyecto(models.Model):
    titulo = models.CharField(max_length=50)
    nombre_mecanico = models.CharField(max_length=60)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=3000)
    nombre_cliente = models.CharField(max_length=60)
    
    def __str__(self):
        return "{} - {}".format(self.titulo, self.nombre_mecanico)

    
