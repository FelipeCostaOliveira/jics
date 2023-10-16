from Classes import *
from registro import *
import os

def cadastro():

  while True:
    nome = input("Digite o nome do discente: ").capitalize()
    matricula = input("Digite a matrícula do discente: ")

    user = registro(nome, matricula)

    while not user.validar_matricula(matricula, 10):
        print("\033[31mMatrícula inválida, digite apenas números com no mínimo 10 algarismos.\033[0m")
        matricula = input("Digite a matrícula do discente:\n ")

    diretorio_raiz = os.getcwd()
    while True:
      if not user.verificar_matricula_em_arquivos(diretorio_raiz, matricula):
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
  caminho = os.path.join(sala, f"{serie}.txt")
  user.exibir_alunos_cadastrados(caminho)


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

  user.exibir_professores_cadastrados()

def acoes():
  while True:
    print("Escolha uma opção: ")
    print("1. Editar aluno")
    print("2. Excluir aluno")
    print("3. Exibir edições")
    print("4. Sair")
    print("5. Cadastrar-se")
    print("6. Exibir alunos cadastrados")
    escolha = int(input("Digite o número da opção desejada"))

    if escolha == 1:
      matricula_atual = input("Digite a matrícula atual do aluno")
      editar_aluno(matricula_atual)
    elif escolha == 2:
      matricula_atual = input("Digite a matrícula atual do aluno")
      excluir_aluno(matricula_atual)
    elif escolha == 3:
      pass
    elif escolha == 4:
      pass
    elif escolha == 5:
      cadastro_professor()
    elif escolha == 6:
      exibir_alunos_cadastrados()
    else:
      print("opção inválida, digite apenas números de 1 a 5")

def exibir_alunos_cadastrados():
  print("\nAlunos cadastrados: ")
  caminho_diretorio = os.getcwd()
  for pasta, _, arquivos in os.walk(caminho_diretorio):
    for arquivo in arquivos:
        if arquivo == "professores_cadastrados.txt" or arquivo == "jogos.txt" or arquivo == "chaves.txt":
          continue
        if arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_txt:
                conteudo = arquivo_txt.read()
                lines = conteudo.splitlines()
                for linha in lines:
                  print(linha)
                 

def editar_aluno(matricula_atual):
    excluir_aluno(matricula_atual)
    nome = input("Digite o nome do discente: ").capitalize()
    matricula = input("Digite a matrícula do discente: ")
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

def excluir_aluno(matricula_atual):
    caminho_diretorio = os.getcwd()
    for pasta, _, arquivos in os.walk(caminho_diretorio):
        for arquivo in arquivos:
            if arquivo in ["professores_cadastrados.txt", "jogos.txt", "chaves.txt"]:
                continue
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(pasta, arquivo)
                linhas_filtradas = []
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_txt:
                    for linha in arquivo_txt:
                        total = linha.split(":")[2].replace(", Curso", "").strip()
                        
                        if total != matricula_atual:
                            linhas_filtradas.append(linha)
                
                with open(caminho_arquivo, "w", encoding="utf-8") as arquivo_txt:
                    #print(linhas_filtradas)
                    arquivo_txt.writelines(linhas_filtradas)
         

