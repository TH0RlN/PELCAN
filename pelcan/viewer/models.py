from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField()
    telefono = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Perro(models.Model):
    nombre = models.CharField(max_length=80)
    raza = models.CharField(max_length=80)
    edad = models.IntegerField()
    peso = models.FloatField()
    foto = models.ImageField(upload_to='storage/img/perros')
    duenho = models.ForeignKey("Cliente", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre    

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    horaFin = models.TimeField()
    perro = models.ForeignKey("Perro", on_delete=models.CASCADE)
    duenho = models.ForeignKey("Cliente", on_delete=models.CASCADE)

    def __str__(self):
        return self.perro.nombre + ' ' + self.fecha.strftime("%d/%m/%Y") + ' ' + self.hora.strftime("%H:%M")