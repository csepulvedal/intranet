from django.contrib import admin

# Register your models here.
from .models import Facultad,Persona,Usuario

admin.site.register(Facultad)
admin.site.register(Persona)
admin.site.register(Usuario)