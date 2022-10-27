#from string import printable
from rest_framework import serializers
from hospitalbackend.models.medico import Medico

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id','especialidad','registro','usuario']