from rest_framework import generics, status
from rest_framework.response import Response
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalbackend.serializers.doctorSerializer import DoctorSerializer
from hospitalbackend.serializers.userSerializer import UserSerializer
from hospitalbackend.models.medico import Usuario


class DoctorListCreateview(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = DoctorSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los medicos")
        queryset = self.get_queryset()
        serializer = DoctorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Medico")
        print(request.data)

        #Extra los datos del usuario del json del request
        usuarioData = request.data.pop("usuario")
        #Se hace un llamado al serializador para que cree un usuario con los datos que se
        #extrajeron del json del request
        ###El serializador se encarga de validar las reglas definidas en el modelo
        serializer_user = UserSerializer(data=usuarioData)
        # Si la infromacion no es valida lanza una exepcion
        serializer_user.is_valid(raise_exception=True)
        #Si la informacion es acorde, el serializer guarda el objeto en la variable usuario
        usuario = serializer_user.save()
        #almacena el restante de la data del json a una variable
        docData = request.data
        #Para crear un medico se necesita la FK del usuario
        #al dicionario que almacenamos con la data restante del request lo actualizamos
        #(agregamos) el id del usuario(utilizando el dic creado anteriormente para los datos del usuario)
        docData.update({"usuario": usuario.id}) #el nombre de la llave es usuario (asi como lo tenemos en el modelo)
        serializer_doc = DoctorSerializer(data=docData)
        serializer_doc.is_valid(raise_exception=True)
        serializer_doc.save()
        return Response(status=status.HTTP_201_CREATED)

        # tokenData = {
        #     "username":request.data["username"],
        #     "password":request.data["password"],
        # }
        # tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        # tokenSerializer.is_valid(raise_exception=True)
        #return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

class DoctorRetriveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = "id"              #Campo con el que se realizan la busquedad de los objects
    lookup_url_kwarg = "pk"           #Nombre dado en la url al argumento
    #permission_classes = (IsAuthenticate,)

    def get(self, request, *args, **kwargs):
        print("GET a Medico")
        queryset = self.get_queryset()
        serializer = DoctorSerializer(queryset)
        # if valid_data('user_id') != kwargs['pk']:
        #     stringResponse =  {'detail':'Unathorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("POST a Medico")
        # if valid_data('user_id') != kwargs['pk']:
        #     stringResponse =  {'detail':'Unathorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Medico")
        # if valid_data('user_id') != kwargs['pk']:
        #     stringResponse =  {'detail':'Unathorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("DELETE a Medico")
        # if valid_data('user_id') != kwargs['pk']:
        #     stringResponse =  {'detail':'Unathorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)