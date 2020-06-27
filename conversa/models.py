from django.db import models
from usuario.models import Professor, Aluno
from aula.models import Aula
import datetime

class Mensagem(models.Model):
    texto = models.CharField(max_length=200, blank=False, null=False)
    imagem = models.CharField(max_length=600, blank=True, null=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto

    def __unicode__(self):
        return self.texto


