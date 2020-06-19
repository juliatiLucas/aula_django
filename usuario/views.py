from rest_framework import views, response, status
from .models import Professor, Aluno
from utils import serializer

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