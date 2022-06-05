from django.contrib import admin

from .models import Aula, Curso

admin.site.register(Curso)
admin.site.register(Aula)
