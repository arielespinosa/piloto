from django.test import TestCase
from django.contrib.auth.models import User
from .modelos.docencia import Ponencia
from .modelos.trabajadores import Trabajador, PersonaExterna
from .modelos.nomencladores import *


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

        campo = CampoEspecialidad.objects.create(nombre='Informatica')
        
        centro_de_estudio = CentroEstudios.objects.create(nombre = "CUJAE", pais = 'Cuba')

        especialidad = Especialidad.objects.create(
            categoria = 'Técnico',
            campo = campo,
            centro_de_estudio = centro_de_estudio
        )

        t = Trabajador.objects.create(
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

        pe = PersonaExterna.objects.create(
            nombre="Fernando",
            apellido1 = "Pacios",
            apellido2 = "Espinosa"
        )

        p = Ponencia.objects.create(
            titulo = 'Ponencia1'
        )

        p.autores.add(t)
        #p.autores.add(pe)

    def test_diferencia_salarial(self):
        trabajador = Trabajador.objects.get(nombre="Antonio")

        self.assertEqual(trabajador.diferencia_salarial, 7)


    def test_ponencias(self):
        trab = Trabajador.objects.get(nombre="Antonio")
        trab_ext = PersonaExterna.objects.get(nombre="Fernando")


        p = Ponencia.objects.get(
            titulo = 'Ponencia1'
        )

        pon = trab.ponencias.get(titulo='Ponencia1')
        pon2 = trab_ext.ponencias.get(titulo='Ponencia1')

        #print(p.autores.trabajador_set)
        print(pon.autores.all())
        print(trab_ext.ponencias.all())

        self.assertTrue(trab in p.autores.all())
        self.assertTrue(trab_ext in p.autores.all())
        self.assertEqual(pon.titulo, 'Ponencia1')
        self.assertEqual(pon, pon2)



















