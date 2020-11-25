from django.test import TestCase
from trabajador.modelos.trabajadores import Trabajador
from trabajador.modelos.nomencladores import Plaza, Oficina, Especialidad, CampoEspecialidad
from docencia.app_models.nomencladores import CentroEstudios
from django.contrib.auth.models import User


class TestRegistrarUsuario(TestCase):

    def setUp(self):
        usuario = User.objects.create(username='tony', password='adminadmin', is_active=False)
        plaza = Plaza.objects.create(
            nombre = "meteorologo",
            grupo_escala_antiguo = "XV",
            grupo_escala_actual = "XX",
            salario_escala_antiguo = 50,
            salario_escala_actual = 60
        )

        oficina = Oficina.objects.create(nombre = "Isra")

        campo = CampoEspecialidad.objects.create(nombre='Informatica')
        
        centro_de_estudio = CentroEstudios.objects.create(nombre = "CUJAE", pais = 'Cuba')

        especialidad = Especialidad.objects.create(
            categoria = 'Técnico',
            campo = campo,
            centro_de_estudio = centro_de_estudio
        )

        Trabajador.objects.create(
            nombre="Antonio",
            apellido1 = "Pacios",
            apellido2 = "Espinosa",
            usuario = usuario,
            ci = "83112829103",
            sexo = "M",
            raza = "M",
            nivel_escolar = "S",
            especialidad = especialidad,    
            tarjeta = 123456,
            plaza = plaza,
            oficina = oficina,
            categoria_ocupacional = "E",
            fecha_entrada_insmet = "2020-10-10",
            direccion = "Madrid"
        )

    def test_registrar_usuario(self):
        trabajador = Trabajador.objects.get(nombre="Antonio")
        self.assertEqual(trabajador.nombre, 'Antonio')
  
    
