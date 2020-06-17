from rest_framework import views, response, status
from .models import Professor, Aluno
from utils import serializer

class ProfessorView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
       
        verify = Professor.objects.filter(email=data['email'], senha=data['senha'])
        if (len(verify) == 0):
            professor = Professor(nome=data['nome'], email=data['email'], senha=data['senha'])
            professor.save()
            return response.Response(serializer.professor_to_json(professor), status.HTTP_201_CREATED)
        else: 
            return response.Response({}, status.HTTP_400_BAD_REQUEST)
    

class AlunoView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
       
        verify = Aluno.objects.filter(email=data['email'], senha=data['senha'])
        if (len(verify) == 0):
            aluno = Aluno(nome=data['nome'], email=data['email'], senha=data['senha'])
            aluno.save()
            return response.Response(serializer.aluno_to_json(aluno), status.HTTP_201_CREATED)
        else: 
            return response.Response({}, status.HTTP_400_BAD_REQUEST)

    # def get(self, request, **kwargs):


class LoginView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        if data['tipo_usuario'] == 'professor':
            try:
                professor = Professor.objects.get(email=data['email'], senha=data['senha'])
                return response.Response(serializer.professor_to_json(professor), status.HTTP_201_CREATED)
            except: 
                return response.Response({}, status.HTTP_400_BAD_REQUEST)
        elif data['tipo_usuario'] == 'aluno':
            try:
                aluno = Aluno.objects.get(email=data['email'], senha=data['senha'])
                return response.Response(serializer.aluno_to_json(aluno), status.HTTP_201_CREATED)
            except: 
                return response.Response({}, status.HTTP_400_BAD_REQUEST)