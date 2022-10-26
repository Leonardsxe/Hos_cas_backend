from django.db import models
from .usuario import Usuario
from .medico import Medico

class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #Usuario_id
    #(Nombbre_variable) = se inicializa la variable como  tipo (model.(nombre_del_campo)(recibe multiples parametros, el primer parametro siendo una FK
    # es a el modelo que esta relacionado, parametro related_name: es para darle el nombre con que queremos que se guarde en la DB))
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
