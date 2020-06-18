from rest_framework import views, response, status
from .models import Aula, AulaAluno
from usuario.models import Professor
from utils import serializer


class AulaView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        professor = Professor.objects.get(pk=data['professor'])
        aula = Aula(nome=data['nome'], professor=professor, data=data['data'])
        aula.save()
        return response.Response(serializer.aula(aula), status=status.HTTP_201_CREATED)
    
    def get(self, request, **kwargs):
        professor = self.kwargs['professor']
        aulas: list = [serializer.aula(aula) for aula in Aula.objects.filter(professor=professor)]

        return response.Response(aulas, status=status.HTTP_200_OK)


class AulaAlunoView(views.APIView):
    def get(self, request, **kwargs):
        aluno = self.kwargs['aluno']
        aulas: list = [serializer.aula_aluno(aula) for aula in AulaAluno.objects.filter(aluno=aluno)]

        return response.Response(aulas, status=status.HTTP_200_OK)
