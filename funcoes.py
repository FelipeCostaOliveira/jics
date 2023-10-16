import os
class registro:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def validar_matricula(self, matricula, x):
        return matricula.isdigit() and len(matricula) >= x

    def verificar_matricula_em_arquivos(self, caminho_diretorio, matricula):
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
                                    return True
        return False


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

    