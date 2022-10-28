from rest_framework import generics, status
from rest_framework.response import Response
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalbackend.serializers.userSerializer import UserSerializer
from hospitalbackend.models.usuario import Usuario


class UserListview(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los usuarios")
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"              #Campo con el que se realizan la busquedad de los objects
    lookup_url_kwarg = "pk"           #Nombre dado en la url al argumento
    permission_classes = (IsAuthenticate,)

    def get(self, request, *args, **kwargs):
        print("GET a Usuario")
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset)
        # if valid_data('user_id') != kwargs['pk']:
        #     stringResponse =  {'detail':'Unathorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("POST a Usuario")
        # if valid_data('user_id') != kwargs['pk']:
        #     stringResponse =  {'detail':'Unathorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        print("PUT a Usuario")
        # if valid_data('user_id') != kwargs['pk']:
        #     stringResponse =  {'detail':'Unathorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("DELETE a Usuario")
        # if valid_data('user_id') != kwargs['pk']:
        #     stringResponse =  {'detail':'Unathorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)