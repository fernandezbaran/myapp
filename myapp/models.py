from django.db import models

class FormResponse(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    dni = models.CharField(max_length=100, null=True)
    motivo_de_consulta = models.CharField(max_length=500, null=True)
    sangrado = models.BooleanField(default=False)
    paralisis_facial = models.BooleanField(default=False)
    debilidad_miembros = models.BooleanField(default=False)
    alteraciones_equilibrio = models.BooleanField(default=False)
    alteraciones_visuales = models.BooleanField(default=False)
    dolor_torax = models.BooleanField(default=False)
    dolor_abdominal = models.BooleanField(default=False)
    dolor_abdominal_mayor_50 = models.BooleanField(default=False)
