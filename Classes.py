import os, sys
import random
import itertools
from datetime import datetime, timedelta
import funcoes
# --------------RENAN / DENY---------------------#
class Pessoa:
    def __init__(self, nome, matricula):
        self._nome = nome   # Convenção para indicar campo protegido
        self.__matricula = matricula  # Convenção para indicar campo privado
    def get_nome(self):
        return self._nome
        # Retorna o valor do campo "nome"

    def set_nome(self, novo_nome):
        self._nome = novo_nome
        # Define um novo valor para o campo "nome"
    def get_matricula(self):
        return self.__matricula
        # Retorna o valor do campo "matricula"

class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso, turma):
        super().__init__(nome, matricula)
        self.curso = curso   
        self.__turma = turma 
    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula
        # Define um novo valor para o campo "matricula"

    def get_turma(self):
        return self.__turma
        # Retorna o valor do campo "turma"

    def set_turma(self, nova_turma):
        self.__turma = nova_turma
        # Define um novo valor para o campo "turma"

    
    def exibir_cadastro(self, sala, serie):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Curso: {sala}")
        print(f"Turma: {serie}")
        print()

    def cadastrar_aluno(self, serie, sala):
        funcoes.gerar_dir(sala)

        caminho = os.path.join(sala, f"{serie}.txt")
        # Abrir o arquivo em modo de adição
        with open(caminho, "a", encoding="utf-8") as arquivo :
        # Escrever os dados do aluno no arquivo
            arquivo.write(f" Nome: {self.get_nome()}, Número Matrícula: {self.get_matricula()}, Curso: {sala} Turma: {serie}\n")
    

class professor(Pessoa):
    def __init__(self, nome, matricula, senha):
        super().__init__(nome, matricula)
        self.__senha = senha
        def get_senha(self):
          return self.__senha
        def set_senha(self, nova_senha):
          self.__senha = nova_senha
          
    def cad_professor(self, senha): 
      funcoes.gerar_dir("Arquivo") 
      caminho = os.path.join("Arquivos", "Professores_cadastrados.txt")     
      with open(caminho, "a", encoding="utf-8") as arquivo :
        # Escrever os dados do professor no arquivo
        arquivo.write(f" Nome: {self.get_nome()}, Número Matrícula: {self.get_matricula()}, Senha: {senha}\n")

class chave:
    def __init__(self, equipe, tam_chave):
        self.caminho = equipe
        self.tam_chave = tam_chave
        
    def gerar_chave(self):
        equipes_cadastradas = []
        for pasta, _, arquivos in os.walk(self.caminho):
            for arquivo in arquivos:
                if arquivo == "professores_cadastrados.txt":
                    continue
                if arquivo.endswith(".txt"):
                    caminho_arquivo = os.path.join(pasta, arquivo)
                    with open(caminho_arquivo, "r", encoding="utf-8") as arq_txt:
                        conteudo = arq_txt.read()
                        linhas = conteudo.splitlines()
                        for linha in linhas:
                            if "Curso:" in linha:
                                palavras = linha.split()  # Dividir a linha em palavras
                                indice_curso = palavras.index("Curso:")
                                curso = palavras[indice_curso + 1]
                                turma = palavras[indice_curso + 3]
                                Equipe = f"{curso}-{turma}"
                                equipes_cadastradas.append(Equipe)
        random.shuffle(equipes_cadastradas)
        num_equipes = len(equipes_cadastradas)
        funcoes.gerar_dir("Arquivos")
        caminho_comp = os.path.join("Arquivos", "chaves.txt")
        with open(caminho_comp, "w", encoding="utf-8") as chvs:
            for i in range(0, num_equipes, self.tam_chave):
                chave = f"Chave {i // self.tam_chave + 1}: {' | '.join(equipes_cadastradas[i:i+self.tam_chave])}\n"
                chvs.write(chave)
                print(chave)

class jogos:
    def __init__(self, chaves, inicio):
        self.chaves = chaves
        self.inicio = inicio   
        self.jogos = {}
    
    def gerar_jogos(self):
        sorteio_jogos = {}  
        with open(self.chaves, "r", encoding="utf-8") as arquivo_chaves:
            conteudo = arquivo_chaves.read()
            linhas = conteudo.splitlines()
            for linha in linhas:
                palavras = linha.split(":")
                chave, equipes = palavras[0], palavras[1].split("|")
                sorteio_jogos[chave] = equipes
        
        formato_brasil = "%d/%m/%Y %H:%M"
        funcoes.gerar_dir("Arquivos")
        caminho_total = os.path.join("Arquivos", "jogos.txt")
        chaves = list(sorteio_jogos)
        with open(caminho_total, "w", encoding="utf-8") as jgs:
            for i in range(len(sorteio_jogos) * (len(sorteio_jogos) - 1)):
                chave1, chave2 = chaves[i % len(chaves)], chaves[(i + 1) % len(chaves)]
                equipe1, equipe2 = random.choice(sorteio_jogos[chave1]), random.choice(sorteio_jogos[chave2])
                inicio_formatado = self.inicio.strftime(formato_brasil)
                termino = self.inicio + timedelta(minutes=30)
                termino_formatado = termino.strftime(formato_brasil)
                jogo = f"{chave1}: Jogo {i + 1}: {equipe1} vs {equipe2} Início: {inicio_formatado} Término: {termino_formatado}\n"
                jgs.write(jogo)
                self.inicio = termino + timedelta(minutes=5)
                if chave1 not in self.jogos:
                    self.jogos[chave1] = []
                self.jogos[chave1].append(jogo)
        
    def exibir_jogos(self):
        jogos_ordenados = sorted(
                [jogo for jogos in self.jogos.values() for jogo in jogos],
                key=lambda x: int(x.split(": Jogo ")[1].split(":")[0]),
            )
        for jogo in jogos_ordenados:
            print(jogo)

class gerenciar_cadastro_aluno:
    def __init__(self, matricula):
        self.matricula = matricula
      
    def editar_aluno(self):
        self.excluir_aluno(self)
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

    def excluir_aluno(self):
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
                            if linha not in arquivo_txt:
                                break
                            else:
                                total = linha.split(":")[2].replace(", Curso", "").strip()
                                
                                if total != self.matricula:
                                    linhas_filtradas.append(linha)
                    
                    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo_txt:
                        #print(linhas_filtradas)
                        arquivo_txt.writelines(linhas_filtradas)
        


