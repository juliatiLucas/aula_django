from rest_framework import views, response, status
from .models import Aula, AulaAluno, Tarefa
from usuario.models import Professor
from utils import serializer


class AulaView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        professor = Professor.objects.get(pk=data['professor'])
        aula = Aula(nome=data['nome'], professor=professor, data=data['data'])
        aula.save()
        return response.Response(serializer.aula(aula), status=status.HTTP_201_CREATED)
    
    def put(self, request, **kwargs):
        data = request.data
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        Aula.objects.filter(pk=self.kwargs['aula']).update(
            nome=data['nome'] if 'nome' in data else aula.nome,
            descricao=data['descricao'] if 'data' in data else aula.data
        )
        return response.Response(data, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        Aula.objects.filter(pk=self.kwargs['aula']).delete()
        return response.Response({}, status=status.HTTP_200_OK)

    def get(self, request, **kwargs):
        professor = self.kwargs['professor']
        aulas: list = [serializer.aula(aula) for aula in Aula.objects.filter(professor=professor)]

        return response.Response(aulas, status=status.HTTP_200_OK)


class AulaAlunoView(views.APIView):
    def get(self, request, **kwargs):
        aluno = self.kwargs['aluno']
        aulas: list = [serializer.aula(aula_aluno.aula) for aula_aluno in AulaAluno.objects.filter(aluno=aluno)]

        return response.Response(aulas, status=status.HTTP_200_OK)
    
    def put(self, request, **kwargs):
        data = request.data
        aula_aluno = AulaAluno.objects.filter(aula=data['aula'], aluno=data['aluno'])[0]
        AulaAluno.objects.filter(aula=data['aula'], aluno=data['aluno']).update(
            presente=data['presente'] if 'presente' in data else aula_aluno.presente,
        )
        return response.Response(data, status=status.HTTP_200_OK)

class AlunosDaAula(views.APIView):
    def get(self, request, **kwargs):
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        alunos = [serializer.aluno(aula_aluno.aluno) for aula_aluno in AulaAluno.objects.filter(aula=aula)]
        return response.Response(alunos, status=status.HTTP_200_OK)


class TarefaView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        tarefa = Tarefa(aula=aula, descricao=data['descricao'], nome=data['nome'])
        tarefa.save()
        return response.Response(serializer.tarefa(tarefa), status=status.HTTP_201_CREATED)

    def put(self, request, **kwargs):
        data = request.data
        tarefa = Tarefa.objects.get(pk=self.kwargs['tarefa'])
        Tarefa.objects.filter(pk=self.kwargs['tarefa']).update(
            nome=data['nome'] if 'nome' in data else tarefa.nome,
            descricao=data['descricao'] if 'descricao' in data else tarefa.descricao
        )
        return response.Response(data, status=status.HTTP_200_OK)

    def get(self, request, **kwargs):
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        tarefas = [serializer.tarefa(tarefa) for tarefa in Tarefa.objects.filter(aula=aula)]

        return response.Response(tarefas, status=status.HTTP_200_OK)