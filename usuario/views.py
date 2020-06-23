from rest_framework import views, response, status
from .models import Professor, Aluno
from utils import serializer
from django.db.models import Q

class ProfessorView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        try:
            verify = Professor.objects.filter(email=data['email'], senha=data['senha'])
            if (len(verify) == 0):
                professor = Professor(nome=data['nome'], email=data['email'], senha=data['senha'])
                professor.save()
                return response.Response(serializer.professor(professor), status.HTTP_201_CREATED)
            else: 
                return response.Response({}, status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({}, status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        professor = Professor.objects.filter(pk=self.kwargs['professor'])
        Professor.objects.filter(pk=self.kwargs['professor']).update(
            nome=data['nome'] if 'nome' in data else professor.nome,
            email=data['email'] if 'email' in data else professor.email,
            senha=data['senha'] if 'senha' in data else professor.senha
        )
        return response.Response({}, status.HTTP_200_OK)

    def get(self, request, **kwargs):
        professor = Professor.objects.get(pk=self.kwargs['professor'])
        return response.Response(serializer.professor(professor), status.HTTP_200_OK)
    

class AlunoView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        try:
            verify = Aluno.objects.filter(email=data['email'], senha=data['senha'])
            if (len(verify) == 0):
                aluno = Aluno(nome=data['nome'], email=data['email'], senha=data['senha'])
                aluno.save()
                return response.Response(serializer.aluno(aluno), status.HTTP_201_CREATED)
            else: 
                return response.Response({}, status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({}, status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, **kwargs):
        aluno = Aluno.objects.filter(pk=self.kwargs['aluno'])
        Aluno.objects.filter(pk=self.kwargs['aluno']).update(
            nome=data['nome'] if 'nome' in data else aluno.nome,
            email=data['email'] if 'email' in data else aluno.email,
            senha=data['senha'] if 'senha' in data else aluno.senha
        )
        
        return response.Response({}, status.HTTP_200_OK)

    # def get(self, request, **kwargs):
    def get(self, request, **kwargs):
        aluno = Aluno.objects.get(pk=self.kwargs['aluno'])
        return response.Response(serializer.aluno(aluno), status.HTTP_200_OK)
    
class LoginView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        if data['tipo_usuario'] == 'professor':
            try:
                professor = Professor.objects.get(email=data['email'], senha=data['senha'])
                return response.Response(serializer.professor(professor), status.HTTP_200_OK)
            except: 
                return response.Response({}, status.HTTP_400_BAD_REQUEST)
        elif data['tipo_usuario'] == 'aluno':
            try:
                aluno = Aluno.objects.get(email=data['email'], senha=data['senha'])
                return response.Response(serializer.aluno(aluno), status.HTTP_200_OK)
            except: 
                return response.Response({}, status.HTTP_400_BAD_REQUEST)


class BuscarAluno(views.APIView):
    def get(self, request, **kwargs):
        alunos = [
            serializer.aluno(aluno) 
            for aluno in Aluno.objects.filter(Q(nome__istartswith=self.kwargs['busca']) | Q(email__istartswith=self.kwargs['busca']))
        ]
        return response.Response(alunos, status.HTTP_200_OK)