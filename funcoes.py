import os


# def validar_nome(nome):
#     while not nome.replace(" ", "").isalpha():
#         print("\033[31mnome inválido digite apenas letras ou espaços\033[0m")
#         nome = input("Digite o nome: ").capitalize().strip()
#
#
# def validar_matricula(matricula, x):
#
#     while True:
#         if matricula.isdigit() and len(matricula) >= x:
#             break
#         else:
#             print(f"\033[31mMatrícula inválida, digite apenas números com no mínimo {x} algarismos.\033[0m")
#             matricula = input("Digite a matrícula: \n ")


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
                                while matricula == linha.split(":")[2].replace(", Curso", "").strip():
                                    print("\033[31mJá existe um aluno cadastrado com essa matrícula.\033[0m")
                                    matricula = input("Digite a matrícula do discente:\n ")
        break


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


def organizar_horarios():
    caminho_jogos = os.path.join("Arquivos", "jogos.txt")
    hora = []
    chaves = []
    jogos_chaves = {}

    # Ler os jogos do arquivo de saída e identificar as chaves
    with open(caminho_jogos, "r", encoding="utf-8") as arquivo_jogos:
        linhas = arquivo_jogos.read().splitlines()

        for linha in linhas:
            if "Chave" in linha:
                chave = linha.split(":")[0].strip()
                if chave not in chaves:
                    chaves.append(chave)
                    jogos_chaves[chave] = []
            partes = linha.split("|")
            parte_mantida = partes[0].strip()
            parte_retirada = partes[1].strip()
            jogos_chaves[chave].append(parte_mantida)
            hora.append(parte_retirada)

    # Reorganizar os jogos em ordem alternada
    jogos_organizados = []
    num_jogos_por_chave = len(jogos_chaves[chaves[0]])
    for i in range(num_jogos_por_chave):
        for chave in chaves:
            jogos_organizados.append(jogos_chaves[chave][i])

    # Escrever os jogos reorganizados em um novo arquivo
    with open(caminho_jogos, "w", encoding="utf-8") as arquivo_saida:
        for jogo, hora_jogo in zip(jogos_organizados, hora):
            arquivo_saida.write(f"{jogo} | {hora_jogo}\n")


def exibir_jogos():
    with open("Arquivos/jogos.txt", "r", encoding="utf-8") as arquivo_chaves:
        conteudo = arquivo_chaves.read()
        linhas = conteudo.splitlines()
        for linha in linhas:
            print(linha)


def gerar_dir(nome_dir):
    if not os.path.exists(nome_dir):
        os.makedirs(nome_dir)
