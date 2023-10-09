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

    def exibir_alunos_cadastrados(self, caminho):
    # Abrir o arquivo em modo de leitura
        with open(caminho, "r", encoding="utf-8") as arquivo:
            # Ler as linhas do arquivo
            linhas = arquivo.readlines()
            # Imprimir os professores cadastrados
            for linha in linhas:
            # Remover a quebra de linha ao imprimir
                print(linha.rstrip())  

    def exibir_professores_cadastrados(self):
    # 
        with open("professores_cadastrados.txt", "r", encoding="utf-8") as arquivo:
            
            linhas = arquivo.readlines()
            
            for linha in linhas:
            
                campos = linha.rstrip().split(",")
                
                nome = campos[0].split(":")[1].strip()
                
                matricula = campos[1].split(":")[1].strip()
                
                senha = campos[2].split(":")[1].strip()
                # Imprimir as informações formatadas na tela
                print(f"Nome: {nome}, Número de matrícula: {matricula}, Senha: {'*' * len(senha)}")


    