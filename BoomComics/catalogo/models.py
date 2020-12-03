from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

# Esta clase se refiere a la categoria al que pertenece, si es Dc comic , Marvel comic , Manga.
class Tipo(models.Model): 
    
	tipoo = models.CharField(max_length=200)

	def __str__(self):
		return self.tipoo

class Formato(models.Model):

	formatoo = models.CharField(max_length=50)

	def __str__(self):
		return self.formatoo    


class Comic(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    resumen = models.TextField(max_length=10000)
    isbn = models.CharField('ISBN', max_length=13)
    tipo = models.ForeignKey('Tipo',on_delete=models.SET_NULL, null=True)
    formato = models.ForeignKey('Formato',on_delete=models.SET_NULL, null=True)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField( upload_to='images/', null=True, blank=True )


    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('comic-detail', args=[str(self.id)])    

class Autor(models.Model):

	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)

	class Meta: 
		ordering = ['nombre' , 'apellido']

	def get_absolute_url(self):
		return reverse('autor-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.nombre} {self.apellido}'	    
