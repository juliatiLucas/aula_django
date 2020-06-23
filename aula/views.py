from rest_framework import views, response, status
from .models import Aula, AulaAluno, Tarefa, Chamada, DataChamada
from usuario.models import Professor, Aluno
from utils import serializer
import json

class AulaView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        professor = Professor.objects.get(pk=data['professor'])
        aula = Aula(nome=data['nome'], professor=professor)
        aula.save()
        return response.Response(serializer.aula(aula), status=status.HTTP_201_CREATED)
    
    def put(self, request, **kwargs):
        data = request.data
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        Aula.objects.filter(pk=self.kwargs['aula']).update(nome=data['nome'] if 'nome' in data else aula.nome)
        return response.Response(data, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        Aula.objects.filter(pk=self.kwargs['aula']).delete()
        return response.Response({}, status=status.HTTP_200_OK)

    def get(self, request, **kwargs):
        professor = self.kwargs['professor']
        aulas: list = [serializer.aula(aula) for aula in Aula.objects.filter(professor=professor)]

        return response.Response(aulas, status=status.HTTP_200_OK)


class AulaAlunoView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        aula = Aula.objects.get(pk=data['aula'])
        aluno = Aluno.objects.get(pk=data['aluno'])
        verify = AulaAluno.objects.filter(aluno=aluno, aula=aula)
        if (len(verify) == 0):
            aula_aluno = AulaAluno(aula=aula, aluno=aluno)
            aula_aluno.save()
            return response.Response({}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        aluno = self.kwargs['aluno']
        aulas: list = [serializer.aula(aula_aluno.aula) for aula_aluno in AulaAluno.objects.filter(aluno=aluno)]

        return response.Response(aulas, status=status.HTTP_200_OK)
    

    def delete(self, request, **kwargs):
        data = request.data
        AulaAluno.objects.filter(aula=data['aula'], aluno=data['aluno']).delete()
        return response.Response({}, status=status.HTTP_200_OK)


class AlunosDaAula(views.APIView):
    def get(self, request, **kwargs):
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        alunos = [serializer.aluno(aula_aluno.aluno) for aula_aluno in AulaAluno.objects.filter(aula=aula)]
        return response.Response(alunos, status=status.HTTP_200_OK)


class TarefaView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        aula = Aula.objects.get(pk=data['aula'])
        tarefa = Tarefa(
            aula=aula,
            descricao=data['descricao'],
            nome=data['nome'],
            prazo=data['prazo'] if 'prazo' in data else None
            )
        tarefa.save()
        return response.Response(serializer.tarefa(tarefa), status=status.HTTP_201_CREATED)

    def put(self, request, **kwargs):
        data = request.data
        tarefa = Tarefa.objects.get(pk=self.kwargs['tarefa'])
        Tarefa.objects.filter(pk=self.kwargs['tarefa']).update(
            nome=data['nome'] if 'nome' in data else tarefa.nome,
            descricao=data['descricao'] if 'descricao' in data else tarefa.descricao,
            prazo=data['prazo'] if 'prazo' in data else tarefa.prazo
        )
        return response.Response(data, status=status.HTTP_200_OK)

    def get(self, request, **kwargs):
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        tarefas = [serializer.tarefa(tarefa) for tarefa in Tarefa.objects.filter(aula=aula)]

        return response.Response(tarefas, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        Tarefa.objects.filter(pk=self.kwargs['tarefa']).delete()
        return response.Response({}, status=status.HTTP_200_OK)


class DataChamadaView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        data_chamada = DataChamada(data=data['data'], aula=aula)
        data_chamada.save()

        return response.Response(serializer.data_chamada(data_chamada), status=status.HTTP_201_CREATED)
    
    def get(self, request, **kwargs):
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        data_chamadas = [serializer.data_chamada(data_chamada) 
        for data_chamada in DataChamada.objects.filter(aula=aula)]

        return response.Response(data_chamadas, status=status.HTTP_200_OK)


class ChamadaView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        data_chamada = DataChamada.objects.get(pk=self.kwargs['data_chamada'])
        alunos_parsed = json.loads(data['alunos'])
   
        for al in alunos_parsed:
            aluno = Aluno.objects.get(pk=al['id'])
            chamada = Chamada(
                aluno=aluno,
                data_chamada=data_chamada,
                presente=True if al['presente'] == '1' else False
                )
            chamada.save()

        return response.Response({}, status=status.HTTP_201_CREATED)