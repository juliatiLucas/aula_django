from django.contrib import admin
from .models import Aula, AulaAluno, Tarefa, Chamada, DataChamada

admin.site.register(Aula)
admin.site.register(AulaAluno)
admin.site.register(Tarefa)
admin.site.register(Chamada)
admin.site.register(DataChamada)
