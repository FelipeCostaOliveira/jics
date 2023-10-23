from Classes import *


def criar_alunos_em_todas_as_turmas():
    cursos = {
        "1": "Informática",
        "2": "Eletrotécnica",
        "3": "Química",
        "4": "Edificações",
    }
    turmas = {
        "1": "1°A",
        "2": "1°B",
        "3": "2°Mat",
        "4": "2°Vesp",
        "5": "3°Mat",
        "6": "3°Vesp",
    }

    for curso_key, curso_nome in cursos.items():
        for turma_key, turma_nome in turmas.items():
            nome = f"Aluno {curso_nome} {turma_nome}"
            matricula = f"{curso_key}{turma_key}0001"  # Matrícula fictícia

            aluno = Aluno(nome, matricula, curso_nome, turma_nome)
            aluno.cadastrar_aluno(turma_nome, curso_nome)
            print(f"Aluno cadastrado para {curso_nome} - {turma_nome}.\n")


criar_alunos_em_todas_as_turmas()
