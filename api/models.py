from django.db import models


# Create your models here.


class Formulario(models.Model):
    haDictadoPrograma  =models.BooleanField(null=True, blank=True)
    programaSeleccionado = models.CharField(null=True, blank=True, max_length=200)
    memoAdjunto = models.CharField(null=True, blank=True, max_length=200)
    mostrarUsoInternoDireccionEstudios=models.BooleanField(null=True, blank=True)
    nombrePrograma=models.CharField(null=True, blank=True, max_length=500)
    directorPrograma=models.CharField(null=True, blank=True, max_length=500)
    FormularioPrincipalCompleto=models.BooleanField(null=True, blank=True)
    nivelProgramaAcademicoSeleccionado=models.CharField(null=True, blank=True, max_length=500)
    tipoProgramaAcademicoSeleccionado=models.CharField(null=True, blank=True, max_length=500)
    departamento=models.IntegerField(null=True)
    emplazamiento=models.IntegerField(null=True)
    Presencial=models.BooleanField(null=True, blank=True)
    Online=models.BooleanField(null=True, blank=True)
    Hibrida=models.BooleanField(null=True, blank=True)
    Otra=models.BooleanField(null=True, blank=True)
    ADistancia=models.BooleanField(null=True, blank=True)
    Diurna=models.BooleanField(null=True, blank=True)
    Vespertina=models.BooleanField(null=True, blank=True)
    value=models.DateTimeField(null=True)


    





class Departamento(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)


class Sede(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)

class Modulos(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
