from django.db import models
from usuario.models import Professor, Aluno

class Aula(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    data = models.DateTimeField(blank=False, null=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome


class AulaAluno(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return self.aula.nome + aluno.nome

    def __unicode__(self):
        return self.aula.nome + aluno.nome