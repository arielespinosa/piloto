from django.test import TestCase
from django.contrib.auth.models import User
from .app_models.trabajador import Trabajador
from .app_models.nomencladores import *


class TrabajadorTestCase(TestCase):
    
    def setUp(self):
        usuario = User.objects.create(username="arielito", password="adminadmin")
        plaza = Plaza.objects.create(
            nombre = "Informatica",
            grupo_escala_antiguo = "V",
            grupo_escala_actual = "X",
            salario_escala_antiguo = 253.4,
            salario_escala_actual = 589.47
        )
        oficina = Oficina.objects.create(nombre="Isra")

        Trabajador.objects.create(
            nombre = "Ariel",
            apellido1 = "Peñalver",
            apellido2 = "Espinosa",
            usuario = usuario,
            ci = "91112829103",
            sexo = "M",
            raza = "M",
            nivel_escolar = "S",
            especialidad = "T",
            tarjeta = "123",
            plaza = plaza,
            oficina = oficina,
            categoria_ocupacional = "T",
            direccion = "Animas 77 b"
        )

    def test_diferencia_salarial(self):
        trabajador = Trabajador.objects.get(nombre="Ariel")

        self.assertEqual(trabajador.diferencia_salarial, 7)








