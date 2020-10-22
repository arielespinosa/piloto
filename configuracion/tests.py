from django.test import TestCase
from trabajador.app_models.trabajador import Trabajador
from trabajador.app_models.nomencladores import Plaza, Oficina
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

        oficina = Oficina.objects.create(
            nombre = "Isra"
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
            especialidad = "S",    
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
  
    
