from django.contrib import admin

# Register your models here.
from . models import Autor, Comic, Formato, Tipo

admin.site.register(Comic)
admin.site.register(Autor)
admin.site.register(Tipo)
admin.site.register(Formato)
