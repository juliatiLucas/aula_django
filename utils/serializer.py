from usuario.models import Professor, Aluno


def aluno_to_json(aluno, password=False):
    aluno_dict: dict = {
        "id": aluno.id,
        "nome": aluno.nome,
        "email": aluno.email,
    }
    if password:
        aluno_dict['senha'] = aluno.senha
    return aluno_dict


def professor_to_json(professor, password=False):
    professor_dict: dict = {
        "id": professor.id,
        "nome": professor.nome,
        "email": professor.email,
    }
    if password:
        professor_dict['senha'] = professor.senha
    return professor_dict

def aula_to_json(aula):
    return {
        "id": aula.id,
        "nome": aula.nome,
        "professor": professor_to_json(aula.professor),
        "data": aula.data
    }