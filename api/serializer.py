from rest_framework import serializers
from .models import Formulario,Departamento, Sede,Modulos

class FormularioSerializer(serializers.ModelSerializer):

    departamento=serializers.SerializerMethodField()
    sede=serializers.SerializerMethodField()
    estado=serializers.SerializerMethodField()
    revisionDGEC=serializers.SerializerMethodField()
    revisionDIREST=serializers.SerializerMethodField()
    revisionFINANZAS=serializers.SerializerMethodField()

    class Meta:
        model=Formulario
        fields= '__all__'

    def get_departamento(self, inst):
        print(inst.departamento   )
        dep=1
        if inst.departamento:
            dep=inst.departamento
        departamento=Departamento.objects.filter(id=dep).first()
        print (departamento.name)
        return departamento.name

    def get_sede(self, inst):
        sede=1
        if inst.emplazamiento:
            sede=inst.emplazamiento
        sede=Sede.objects.filter(id=sede).first()
        return sede.name
    
    def get_estado(self, inst):
       return "Pendiente"
    
    def get_revisionDGEC(self, inst):
       return False
    
    def get_revisionDIREST(self, inst):
       return False
    
    def get_revisionFINANZAS(self, inst):
       return False

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departamento
        fields= '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sede
        fields= '__all__'

class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Modulos
        fields= '__all__'