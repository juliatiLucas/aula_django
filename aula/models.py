from django.db import models
from usuario.models import Professor, Aluno

class Aula(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
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
        return f'{self.aluno.nome} [{self.aula.nome}]'

    def __unicode__(self):
        return f'{self.aluno.nome} [{self.aula.nome}]'


class Tarefa(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.CharField(max_length=560)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    prazo = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class DataChamada(models.Model):
    data = models.DateField(auto_now_add=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return f'{self.pk} {self.aula.nome} [{str(self.data)}]'

    def __unicode__(self):
        return f'{self.pk} {self.aula.nome} [{str(self.data)}]'


class Chamada(models.Model):
    data_chamada = models.ForeignKey(DataChamada, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.aluno.nome} [{str(self.data_chamada.data)}]'

    def __unicode__(self):
        return f'{self.aluno.nome} [{str(self.data_chamada.data)}]'

