from django.db import models

class Numero(models.Model):
    numero = models.CharField(max_length=15, unique=True)
    es_spam = models.BooleanField(default=False)
    reportes = models.IntegerField(default=0)

    def __str__(self):
        return self.numero

class Reporte(models.Model):
    numero = models.ForeignKey(Numero, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reporte para {self.numero.numero} - {self.fecha}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
