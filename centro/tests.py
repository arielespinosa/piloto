from django.test import TestCase, Client
from .models import *


class TestCentroModels(TestCase):
    def setUp(self): 

        local = Local.objects.create(nombre='asdasd')    
        objeto = Objeto.objects.create(nombre='wwwwwww')     
        Inventario.objects.create(
            fecha='2020-10-10',
            numero='1',
            local=local,
            objeto=objeto,
            estado='En uso',
        )

    def test_models(self):
        inventario = Inventario.objects.get(numero=1)
        self.assertEqual(inventario.numero, '1')

