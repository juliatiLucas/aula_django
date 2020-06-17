from django.db import models


class Professor(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False, unique=True)
    senha = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False, unique=True)
    senha = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome