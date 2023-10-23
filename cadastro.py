from Classes import *
import os
import funcoes


def cadastro():
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
  while True:
    nome = input("Digite o nome do discente: ").capitalize().strip()
    while not nome.replace(" ", "").isalpha():
        print("\033[31mnome inválido digite apenas letras ou espaços\033[0m")
        nome = input("Digite o nome: ").capitalize().strip()

    matricula = input("Digite a matrícula do discente: ")
    while True:
        if matricula.isdigit() and len(matricula) >= 10:
            break
        else:
            print(f"\033[31mMatrícula inválida, digite apenas números com no mínimo 10 algarismos.\033[0m")
            matricula = input("Digite a matrícula: \n ")
    diretorio_raiz = os.getcwd()
    funcoes.verificar_matricula_em_arquivos(diretorio_raiz, matricula)
    print("\nCursos disponíveis:")
    for key, value in cursos.items():
      print(f"{key} - {value}")
    curso = input("\nDigite o número correspondente ao curso do discente: ").capitalize()
    print("\nTurmas disponíveis:")
    for key, value in turmas.items():
      print(f"{key} - {value}")
    turma = input("Digite o número correspondente à turma do discente: ").capitalize()
    if curso in cursos and turma in turmas:
      sala = cursos[curso]
      serie = turmas[turma]
      pessoa = Aluno(nome, matricula, sala, serie)
      pessoa.cadastrar_aluno(serie, sala)
    else:
      print("Opção de curso ou turma inválida.")
    repetir = input("Deseja realizar um novo cadastro?\n1 - \033[032mSim\n\033[0m2 - \033[031mNão \033[0m")
    if repetir == '2':
      break
  print("\n\u001b[1m\033[032mCadastros Realizados na sua turma:\033[0m\n")


def cadastro_professor():
    prof = []
    nome = input("Digite seu nome: ").capitalize()
    while not nome.replace(" ", "").isalpha():
        print("\033[31mnome inválido digite apenas letras ou espaços\033[0m")
        nome = input("Digite o nome: ").capitalize().strip()
    matricula_prof = input("Digite seu número de matrícula: ")
    while True:
        if matricula_prof.isdigit() and len(matricula_prof) >= 5:
            break
        else:
            print(f"\033[31mMatrícula inválida, digite apenas números com no mínimo 5 algarismos.\033[0m")
            matricula_prof = input("Digite a matrícula: \n ")
    diretorio_raiz = os.getcwd()
    funcoes.verificar_matricula_em_arquivos(diretorio_raiz, matricula_prof)
    senha = input("Digite sua senha: ")
    servidor = Professor(nome, matricula_prof, senha)
    prof.append(servidor)
    servidor.cad_professor(senha)
    print("\nCadastro realizado")


def acoes():
    print("Escolha uma opção: ")
    print("1. Cadastrar-se")
    print("2. Editar aluno")
    print("3. Excluir aluno")
    print("4. Gerar chaveamento")
    print("5. Exibir professores cadastrados")
    print("6. Exibir alunos cadastrados")
    print("7. Gerar jogos")
    print("8. Sair")
    while True:
        try:
          escolha = int(input("Digite o número da opção desejada: "))
          if escolha == 1:
            # cadastrar-se
            cadastro_professor()
            break
          elif escolha == 2:
            # editar aluno
            matricula_atual = input("Digite a matrícula atual do aluno: ")
            gerenciar = GerenciarCadastroAluno(matricula_atual)
            gerenciar.editar_aluno()
            break
          elif escolha == 3:
            # excluir aluno
            matricula_atual = input("Digite a matrícula atual do aluno: ")
            gerenciar = GerenciarCadastroAluno(matricula_atual)
            gerenciar.excluir_aluno()
            break
          elif escolha == 4:
            # gerar chaveamento
            caminho_raiz = os.getcwd()
            tamanho = 4
            sistem = Chave(caminho_raiz, tamanho)
            sistem.gerar_chave()
          elif escolha == 5:
            # exibir professores cadastrados
            funcoes.exibir_professores()
          elif escolha == 6:
            # exibir alunos cadastrados
            funcoes.exibir_alunos_cadastrados()
            break
          elif escolha == 7:
              arquivo = "Arquivos/chaves.txt"
              inicio = datetime(2023, 11, 13, 10, 0)
              sortear = Jogos(arquivo, inicio)
              sortear.gerar_jogos()
              sortear.exibir_jogos()

              break
          elif escolha == 8:
            # sair
            break
          else:
            print("opção inválida, digite apenas números de 1 a 5")
        except ValueError:
            print("\033[031mdigite somente números\033[0m")



