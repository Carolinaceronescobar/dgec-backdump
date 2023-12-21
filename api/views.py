from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializer import FormularioSerializer,SedeSerializer,DepartamentoSerializer, ModulosSerializer

from .models import Formulario,Sede,Departamento,Modulos
# Create your views here.
class TestViewset(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer

    @action(methods=["post"], detail=False, url_path="guardarFormulario")
    def test(self, request):
        try:
          print(request)
          print('aca  v2')
          return Response({"message": "ok"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        

class DepartamentoViewset(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class SedeViewset(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
class ModulosViewset(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    serializer_class = ModulosSerializer