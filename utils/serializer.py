from aula.models import Chamada

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
        "data": aula.data,
        "professor": professor(aula.professor)
    }

def aula_aluno(aula_aluno):
    return {
        "id": aula_aluno.id,
        "aula": aula(aula_aluno.aula),
        "aluno": aluno(aula_aluno.aluno)
    }

def tarefa(tarefa):
    return {
        "id": tarefa.id,
        "nome": tarefa.nome,
        "descricao": tarefa.descricao,
        "prazo": tarefa.prazo,
        "aula": aula(tarefa.aula)
    }

def mensagem(mensagem):
    return {
        "id": mensagem.id,
        "texto": mensagem.texto,
        "imagem": mensagem.imagem,
        "aula": aula(mensagem.aula),
        "professor": professor(mensagem.professor) if mensagem.professor else None,
        "aluno": aluno(mensagem.aluno) if mensagem.aluno else None
    }


def data_chamada(data_chamada):
    return {
        "id": data_chamada.id,
        "aula": data_chamada.aula.id,
        "data": data_chamada.data,
        "chamadas": [chamada(c) for c in Chamada.objects.filter(data_chamada=data_chamada)]
    }

def chamada(chamada):
    return {
        "id": chamada.id,
        "aluno": aluno(chamada.aluno),
        "presente": chamada.presente,
    }