from django.contrib import admin
from django.urls import path
from usuario.views import ProfessorView, AlunoView, LoginView
from aula.views import AulaView, AulaAlunoView, TarefaView, AlunosDaAula, ChamadaView
from conversa.views import MensagemView

urlpatterns = [
    path('admin/', admin.site.urls),
    #Rotas
    path('professores/', ProfessorView.as_view()),
    path('professores/<int:professor>/', ProfessorView.as_view()),
    path('professores/<int:professor>/aulas/', AulaView.as_view()),
    path('alunos/', AlunoView.as_view()),
    path('alunos/<int:aluno>', AlunoView.as_view()),
    path('alunos/<int:aluno>/aulas/', AulaAlunoView.as_view()),
    path('login/', LoginView.as_view()),
    path('aulas/', AulaView.as_view()),
    path('aulas/<int:aula>/', AulaView.as_view()),
    path('aulas/<int:aula>/alunos', AlunosDaAula.as_view()),
    path('aulas/<int:aula>/chamada/', ChamadaView.as_view()),
    path('aulas/<int:aula>/mensagens/', MensagemView.as_view()),
    path('aulas/<int:aula>/mensagens/<int:mensagem>/', MensagemView.as_view()),
    path('aulas/<int:aula>/tarefas/', TarefaView.as_view()),
    path('tarefas/<int:tarefa>/', TarefaView.as_view()),
    path('tarefas/', TarefaView.as_view()),
    path('presenca/', AulaAlunoView.as_view()),
]
