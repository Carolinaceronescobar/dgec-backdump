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
    departamento=models.CharField(null=True, blank=True, max_length=500)
    emplazamiento=models.IntegerField(null=True, blank=True)
    value=models.DateTimeField(null=True, blank=True)
    sede = models.CharField(max_length=255,null=True, blank=True)
    estado = models.CharField(max_length=50,null=True, blank=True)
    revisionDGEC = models.BooleanField(null=True, blank=True)
    revisionDIREST = models.BooleanField(null=True, blank=True)
    revisionFINANZAS = models.BooleanField(null=True, blank=True)
    haDictadoPrograma = models.BooleanField(null=True, blank=True)
    memoAdjunto = models.FileField(null=True, blank=True)  # Puedes ajustar el tipo de campo según tus necesidades
    mostrarUsoInternoDireccionEstudios = models.BooleanField(null=True, blank=True)
    nombrePrograma = models.CharField(max_length=255, null=True, blank=True)
    directorPrograma = models.CharField(max_length=255, null=True, blank=True)
    FormularioPrincipalCompleto = models.BooleanField(null=True, blank=True)
    nivelProgramaAcademicoSeleccionado = models.CharField(max_length=255, null=True, blank=True)
    tipoProgramaAcademicoSeleccionado = models.CharField(max_length=255, null=True, blank=True)
    emplazamiento = models.IntegerField(null=True, blank=True)
    presencial = models.BooleanField(null=True, blank=True)
    online = models.BooleanField(null=True, blank=True)
    hibrida = models.BooleanField(null=True, blank=True)
    jornada_otra = models.BooleanField(null=True, blank=True, default=False)
    jornada_aDistancia = models.BooleanField(null=True, blank=True, default=False)
    jornada_diurna = models.BooleanField(null=True, blank=True, default=False)
    jornada_vespertina = models.BooleanField(null=True, blank=True, default=False)
    modalidad_presencial = models.BooleanField(null=True, blank=True, default=False)
    modalidad_online = models.BooleanField(null=True, blank=True, default=False)
    modalidad_hibrida = models.BooleanField(null=True, blank=True, default=False)
    modalidad_otra = models.BooleanField(null=True, blank=True, default=False)
    duracion_fecha_inicio = models.CharField(max_length=255,null=True, blank=True)
    duracion_fecha_termino = models.CharField(max_length=255,null=True, blank=True)
    programa_director = models.CharField(max_length=255, null=True, blank=True)
    programa_duracion = models.CharField(max_length=255, null=True, blank=True)
    programa_numero = models.CharField(max_length=255, null=True, blank=True)
    programa_tipo = models.CharField(max_length=255, null=True, blank=True)
    convocatoria_fecha_inicio = models.CharField(max_length=255,null=True, blank=True)
    convocatoria_fecha_termino = models.CharField(max_length=255,null=True, blank=True)
    programa_nivel = models.CharField(max_length=255,null=True, blank=True)
    emplazamiento_int= models.IntegerField(null=True, blank=True)
    departamento_int=  models.IntegerField(null=True, blank=True)
    programa_descripcion = models.CharField(max_length=255,null=True, blank=True)
    programa_objetivo = models.CharField(max_length=255,null=True, blank=True)
    programa_resenia = models.CharField(max_length=500,null=True, blank=True)
    linkedin = models.CharField(max_length=500,null=True, blank=True)
    programa_resenia_dos = models.CharField(max_length=500,null=True, blank=True)
    linkedin_dos = models.CharField(max_length=500,null=True, blank=True)
    cedula = models.BooleanField(null=True, blank=True, default=False)
    cedula = models.BooleanField(null=True, blank=True, default=False)
    licenciaMedia = models.BooleanField(null=True, blank=True, default=False)
    curriculum = models.BooleanField(null=True, blank=True, default=False)
    otra = models.BooleanField(null=True, blank=True, default=False)
    cupo_maximo = models.CharField(max_length=250,null=True, blank=True)
    cupo_minimo = models.CharField(max_length=250,null=True, blank=True)
    profesores = models.CharField(max_length=500,null=True, blank=True)
    arancel = models.CharField(max_length=500,null=True, blank=True)
    mujeres = models.BooleanField(null=True, blank=True, default=False)
    mujeresText = models.CharField(max_length=500,null=True, blank=True)
    funcionariosUSM = models.BooleanField(null=True, blank=True, default=False)
    funcionariosUSMText = models.CharField(max_length=500,null=True, blank=True)
    funcionariosServiciosPublicos = models.BooleanField(null=True, blank=True, default=False)
    funcionariosServiciosPublicosText = models.CharField(max_length=500,null=True, blank=True)
    matriculaAnticipada = models.BooleanField(null=True, blank=True, default=False)
    matriculaAnticipadaText = models.CharField(max_length=500,null=True, blank=True)
    otros = models.BooleanField(null=True, blank=True, default=False)
    otrosText = models.CharField(max_length=500,null=True, blank=True)
    otrosDesc = models.CharField(max_length=500,null=True, blank=True)
    postulante_cedula = models.BooleanField(null=True, blank=True, default=False)
    postulante_licenciaMedia = models.BooleanField(null=True, blank=True, default=False)
    postulante_curriculum = models.BooleanField(null=True, blank=True, default=False)
    postulante_otra = models.BooleanField(null=True, blank=True, default=False)
    dcto_exAlumnosUSM = models.BooleanField(null=True, blank=True, default=False)
    dcto_exAlumnosUSMText  = models.CharField(max_length=250,null=True, blank=True)
    dcto_mujeres = models.BooleanField(null=True, blank=True, default=False)
    dcto_mujeresText  = models.CharField(max_length=250,null=True, blank=True)
    dcto_funcionariosUSM = models.BooleanField(null=True, blank=True, default=False)
    dcto_funcionariosUSMText  = models.CharField(max_length=250,null=True, blank=True)
    dcto_funcionariosServiciosPublicos = models.BooleanField(null=True, blank=True, default=False)
    dcto_funcionariosServiciosPublicosText  = models.CharField(max_length=250,null=True, blank=True)
    dcto_matriculaAnticipada = models.BooleanField(null=True, blank=True, default=False)
    dcto_matriculaAnticipadaText  = models.CharField(max_length=250,null=True, blank=True)
    dcto_otros = models.BooleanField(null=True, blank=True, default=False)
    dcto_otrosDesc = models.CharField(max_length=250,null=True, blank=True)
    dcto_otrosText  = models.CharField(max_length=250,null=True, blank=True)
    modalidad_pago=models.CharField(max_length=250,null=True, blank=True)





class Modalidad_Pago(models.Model):
    nombre = models.CharField(max_length=250,null=True, blank=True)
    
    
    
class Departamento(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)


class Sede(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)

class Modulos(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
