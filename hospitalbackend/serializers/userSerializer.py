#from string import printable
from rest_framework import serializers
from hospitalbackend.models.usuario import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','rol','username','password','nombre','apellido','email','celular','direccion']