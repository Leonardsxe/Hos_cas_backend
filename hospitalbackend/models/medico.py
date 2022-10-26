from unittest.util import _MAX_LENGTH
from django.db import models
from .usuario import Usuario

class Medico(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name="medico", on_delete=models.CASCADE)
    especialidad = models.CharField('Especialidad',max_length= 20)
    registro = models.CharField('Tarjeta profecional', max_length=20)