from Classes import *
from funcoes import *
import os
import funcoes
def cadastro():

  while True:
    nome = input("Digite o nome do discente: ").capitalize().strip()
    funcoes.validar_nome(nome)
    matricula = input("Digite a matrícula do discente: ")

    funcoes.validar_matricula(matricula, 10)
        

    diretorio_raiz = os.getcwd()
    
    funcoes.verificar_matricula_em_arquivos(diretorio_raiz, matricula)
       
      

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

    pessoa = Aluno(nome, matricula, curso, turma)
    print("\n\u001b[1m\033[032mCadastro realizado com sucesso!\033[0m\n")

    if curso == "1":
      sala = "Informática"
    elif curso == "2":
      sala = "Eletrotécnica"
    elif curso == "3":
      sala = "Química"
    elif curso == "4":
      sala = "Edificações"

    if turma == "1":
      serie = "1°A"
    elif turma == "2":
      serie = "1°B"
    elif turma == "3":
      serie = "2°Mat"
    elif turma == "4":
      serie = "2°Vesp"
    elif turma == "5":
      serie = "3°Mat"
    elif turma == "6":
      serie = "3°Vesp"


    pessoa.cadastrar_aluno(serie, sala)

    repetir = input("Deseja realizar um novo cadastro?\n1 - \033[032mSim\n\033[0m2 - \033[031mNão \033[0m")
    if repetir == '2':
      break
  print("\n\u001b[1m\033[032mCadastros Realizados na sua turma:\033[0m\n")
 


def cadastro_professor():
  prof = []
  nome = input("Digite seu nome: ").capitalize()

  matricula_prof = input("Digite seu número de matrícula: ")
  user = registro(nome, matricula_prof)
  while not user.validar_matricula(matricula_prof, 5):
      print("\033[31mMatrícula inválida, digite apenas números com no mínimo 5 algarismos.\033[0m")
      matricula_prof = input("Digite seu número de matrícula: \n ")

  diretorio_raiz = os.getcwd()
  while True:
      if not user.verificar_matricula_em_arquivos(diretorio_raiz, "professores_cadastrados.txt"):
        break
      print("\033[31mJá existe um professor cadastrado com essa matrícula.\033[0m")
      matricula = input("Digite seu número de matrícula: \n ")

  senha = input("Digite sua senha: ")
  servidor = professor(nome, matricula_prof, senha)
  prof.append(servidor)
  servidor.cad_professor(senha)
  print("\nProfessores cadastrados")

def acoes():
  while True:
    print("Escolha uma opção: ")
    print("1. Editar aluno")
    print("2. Excluir aluno")
    print("3. Exibir edições")
    print("4. Sair")
    print("5. Cadastrar-se")
    print("6. Exibir alunos cadastrados")
    print("7. Exibir professores cadastrados")
    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
      matricula_atual = input("Digite a matrícula atual do aluno")
      gerenciar = gerenciar_cadastro_aluno(matricula_atual)
      gerenciar.editar_aluno()
      break
    elif escolha == 2:
      matricula_atual = input("Digite a matrícula atual do aluno")
      gerenciar = gerenciar_cadastro_aluno(matricula_atual)
      gerenciar.excluir_aluno()
      break
    elif escolha == 3:
      pass
      break
    elif escolha == 4:
      break
    elif escolha == 5:
      cadastro_professor()
      break
    elif escolha == 6:
      funcoes.exibir_alunos_cadastrados()
      break
    elif escolha == 7:
      funcoes.exibir_professores()
      break
    else:
      print("opção inválida, digite apenas números de 1 a 5")

