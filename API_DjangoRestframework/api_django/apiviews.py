from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Producto, Categoria, SubCategoria
from .serializers import ProductoSerializer, CategoriaSerializer, SubcategoriaSerielizer, \
    UserSerializer
from django.contrib.auth import authenticate

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetalle(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class SubCategoriaSave(generics.CreateAPIView):
    serializer_class = SubcategoriaSerielizer


class SubCategoriaList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset
    serializer_class = SubcategoriaSerielizer

class SubCategoriaAdd(APIView):
    def post(self, request, cat_pk):
        descripcion = request.data.get("descripcion")
        data = {"categoria":cat_pk, 'descripcion':descripcion}
        serializer = SubcategoriaSerielizer(data=data)
        if serializer.is_valid():
            subcat = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Credenciales Incorrectas"},
                            status=status.HTTP_400_BAD_REQUEST)