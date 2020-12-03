from django.test import TestCase
from catalogo.models import Autor , Formato

class TestModelAutor(TestCase):
    @classmethod
    def setUpTestData(cls):
        Autor.objects.create(nombre='Geoff', apellido='Johns')
    def test_nombre_label(self) :
        autor= Autor.objects.get(id=1)
        field_label = autor._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')


class TestModelFormato(TestCase):
    @classmethod
    def setUpTestData(cls):
        Formato.objects.create(formatoo='Cartone')
    def test_formatoo_label(self) :
        formaat= Formato.objects.get(id=1)
        field_label = formaat._meta.get_field('formatoo').verbose_name
        self.assertEquals(field_label,'formatoo')