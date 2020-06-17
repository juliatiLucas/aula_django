from django.contrib import admin
from django.urls import path
from usuario.views import ProfessorView, AlunoView, LoginView
from aula.views import AulaView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('professores/', ProfessorView.as_view()),
    path('professores/<int:professor>/aulas/', AulaView.as_view()),
    path('alunos/', AlunoView.as_view()),
    path('login/', LoginView.as_view()),
    path('aulas/', AulaView.as_view()),
    path('aulas/<int:aula>/', AulaView.as_view()),

]
