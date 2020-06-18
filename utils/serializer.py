from usuario.models import Professor, Aluno


def aluno(aluno, password=False):
    aluno_dict: dict = {
        "id": aluno.id,
        "nome": aluno.nome,
        "email": aluno.email,
    }
    if password:
        aluno_dict['senha'] = aluno.senha
    return aluno_dict
 

def professor(professor, password=False):
    professor_dict: dict = {
        "id": professor.id,
        "nome": professor.nome,
        "email": professor.email,
    }
    if password:
        professor_dict['senha'] = professor.senha
    return professor_dict

def aula(aula):
    return {
        "id": aula.id,
        "nome": aula.nome,
        "professor": professor(aula.professor),
        "data": aula.data
    }

def aula_aluno(aula_aluno):
    return {
        "id": aula_aluno.id,
        "aula": aula(aula_aluno.aula),
        "aluno": aluno(aula_aluno.aluno)
    }