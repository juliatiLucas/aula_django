from rest_framework import views, response, status
from .models import Mensagem
from aula.models import Aula
from usuario.models import Professor, Aluno
from utils import serializer

class MensagemView(views.APIView):
    def post(self, request, **kwargs):
        data = request.data
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        professor = Professor.objects.get(pk=data['professor']) if 'professor' in data else None
        aluno = Aluno.objects.get(pk=data['aluno']) if 'aluno' in data else None

        mensagem = Mensagem(
            texto=data['texto'] if 'texto' in data else '',
            imagem=data['imagem'] if 'imagem' in data else '',
            aula=aula,
            aluno=aluno,
            professor=professor
        )
        mensagem.save()
        return response.Response(serializer.mensagem(mensagem), status.HTTP_201_CREATED)

    #/aulas/<int:aula>/mensagens
    def get(self, request, **kwargs):
        aula = Aula.objects.get(pk=self.kwargs['aula'])
        mensagens = [serializer.mensagem(mensagem) for mensagem in Mensagem.objects.filter(aula=aula)]
        return response.Response(mensagens, status.HTTP_200_OK)


    def delete(self, request, **kwargs):
        Mensagem.objects.filter(pk=self.kwargs['mensagem']).delete()
        return response.Response({}, status.HTTP_200_OK)