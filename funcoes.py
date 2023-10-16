import os

def validar_nome(nome):
    while not nome.replace(" ","").isalpha():
      print("nome inválido digite apenas letras ou espaços")
      nome = input("Digite o nome do discente: ").capitalize().strip()

def validar_matricula(matricula, x):

    while True:
        if matricula.isdigit() and len(matricula) >= x:
            break
        else:
            print("\033[31mMatrícula inválida, digite apenas números com no mínimo 10 algarismos.\033[0m")
            matricula = input("Digite a matrícula do discente:\n ")

def verificar_matricula_em_arquivos(caminho_diretorio, matricula):
    while True:
        for pasta, _, arquivos in os.walk(caminho_diretorio):
            for arquivo in arquivos:
                if arquivo.endswith(".txt"):
                    caminho_arquivo = os.path.join(pasta, arquivo)
                    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_txt:
                        conteudo = arquivo_txt.read()
                        for linha in conteudo.splitlines():
                            if linha.strip() == "":
                                break
                            if len(linha.split(":")) >= 3:
                                if matricula == linha.split(":")[2].replace(", Curso", "").strip():
                                    break
                                else:
                                    print("\033[31mJá existe um aluno cadastrado com essa matrícula.\033[0m")
                                    matricula = input("Digite a matrícula do discente:\n ")
        

def exibir_alunos_cadastrados():
        print("\033[032m\nAlunos cadastrados: \033[0m")
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

def exibir_professores():
    print("\n\033[032mProfessores Cadastrados \033[0m")
    caminho_arquivo = os.path.join("Arquivos", "Professores_cadastrados.txt")    
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_txt:
        conteudo = arquivo_txt.read()
        lines = conteudo.splitlines()
        for linha in lines:
          print(linha)

def gerar_dir(nome_dir):
    if not os.path.exists(nome_dir):
        os.makedirs(nome_dir)

    