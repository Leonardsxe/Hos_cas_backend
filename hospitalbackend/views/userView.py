from rest_framework import generics, views
from rest_framework.response import Response
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalbackend.serializers.userSerializer import UserSerializer
from hospitalbackend.models.usuario import Usuario


class UserListCreateview(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los usuarios")
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a usuarios")
        print(request.data)
        usuarioData = request.data.pop("usuario")
        serializer_user = UserSerializer(data=usuarioData)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save()
        return Response(status=status.HTTP_201_CREATED)

class UserRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset =