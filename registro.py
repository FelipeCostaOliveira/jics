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

    


    