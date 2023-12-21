from rest_framework import routers
from django.urls import path, include


from .views import (

    TestViewset,
    DepartamentoViewset,
    SedeViewset,
    ModulosViewset
   
)

router = routers.SimpleRouter()
router.trailing_slash = "/?"
router.register(r"formulario", TestViewset, basename="test")
router.register(r"sede", SedeViewset, basename="sede")
router.register(r"departamento", DepartamentoViewset, basename="departamento")
router.register(r"modulos", ModulosViewset, basename="modulos")





urlpatterns = [
    path("", include(router.urls)),
]