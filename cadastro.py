from Equipe import Aluno, Professor
from registro import Registro
import os

class Cadastro:
    def __init__(self):
        self.registro = Registro()

    def cadastro_aluno(self):
        while True:
            nome = input("Digite o nome do discente: ").capitalize()
            matricula = input("Digite a matrícula do discente: ")

            while not self.registro.validar_matricula(matricula, 10):
                print("\033[31mMatrícula inválida, digite apenas números com no mínimo 10 algarismos.\033[0m")
                matricula = input("Digite a matrícula do discente:\n ")

            diretorio_raiz = os.getcwd()
            while True:
                if not self.registro.verificar_matricula_em_arquivos(diretorio_raiz, matricula):
                    break
                print("\033[31mJá existe um aluno cadastrado com essa matrícula.\033[0m")
                matricula = input("Digite a matrícula do discente:\n ")

            print(
                "\n \033[0mCursos disponíveis:\033[0m\n1 - \033[034mInformática\033[0m\n2 - \033[032mEletrotécnica\033[0m\n3 - \033[035mQuímica\033[0m\n4 - \033[031mEdificações\033[0m"
            )
            curso = input(
                "\nDigite o número correspondente ao curso do discente: ").capitalize()

            print(
                "\n\033[033mTurmas disponíveis:\n\033[0m1 - 1°A\n2 - 1°B\n3 - 2°Mat\n4 - 2°Vesp\n5 - 3°Mat\n6 - 3°Vesp"
            )
            turma = input(
                "Digite o número correspondente à turma do discente: ").capitalize()

            aluno = Aluno(nome, matricula, curso, turma)
            print("\n\u001b[1m\033[032mCadastro realizado com sucesso!\033[0m\n")

            aluno.cadastrar_aluno()

            repetir = input("Deseja realizar um novo cadastro?\n1 - \033[032mSim\n\033[0m2 - \033[031mNão \033[0m")
            if repetir == '2':
                break

        print("\n\u001b[1m\033[032mCadastros Realizados na sua turma:\033[0m\n")
        caminho = os.path.join(curso, f"{turma}.txt")
        self.registro.exibir_alunos_cadastrados(caminho)

    def cadastro_professor(self):
        professores = []
        nome = input("Digite seu nome: ").capitalize()

        matricula_prof = input("Digite seu número de matrícula: ")

        while not self.registro.validar_matricula(matricula_prof, 5):
            print("\033[31mMatrícula inválida, digite apenas números com no mínimo 5 algarismos.\033[0m")
            matricula_prof = input("Digite seu número de matrícula: \n ")

        diretorio_raiz = os.getcwd()
        while True:
            if not self.registro.verificar_matricula_em_arquivos(diretorio_raiz, "professores_cadastrados.txt"):
                break
            print("\033[31mJá existe um professor cadastrado com essa matrícula.\033[0m")
            matricula_prof = input("Digite seu número de matrícula: \n ")

        senha = input("Digite sua senha: ")
        professor = Professor(nome, matricula_prof, senha)
        professores.append(professor)
        professor.cadastrar_professor(senha)
        print("\nProfessores cadastrados")

        self.registro.exibir_professores_cadastrados()

cadastro = Cadastro()
cadastro.cadastro_aluno()
cadastro.cadastro_professor()
