from rest_framework import serializers
from .models import Formulario,Departamento, Sede,Modulos

class FormularioSerializer(serializers.ModelSerializer):

    departamento=serializers.SerializerMethodField(required=False)
    sede=serializers.SerializerMethodField(required=False)
    estado=serializers.SerializerMethodField(required=False)
    revisionDGEC=serializers.SerializerMethodField(required=False)
    revisionDIREST=serializers.SerializerMethodField(required=False)
    revisionFINANZAS=serializers.SerializerMethodField(required=False)

    class Meta:
        model=Formulario
        fields= '__all__'

    def get_departamento(self, inst):
        try:
            dep=1
            if inst.departamento:
                dep=inst.departamento
            departamento=Departamento.objects.filter(id=dep).first()
            print (departamento.name)
            return departamento.name
        except:
            return ''

    def get_sede(self, inst):
        try:
            sede=1
            if inst.emplazamiento:
                sede=inst.emplazamiento
            sede=Sede.objects.filter(id=sede).first()
            return sede.name
        except:
            return ''
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