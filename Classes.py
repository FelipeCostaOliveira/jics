import os, sys
import random
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
        self.curso = curso   # Campo público
        self.__turma = turma  # Convenção para indicar campo privado

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
    #cria repositório
        if not os.path.isdir(sala):
            os.mkdir(sala)  

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
      with open("professores_cadastrados.txt", "a", encoding="utf-8") as arquivo :
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
                                Equipe = f"{curso} {turma}"
                                equipes_cadastradas.append(Equipe)
        random.shuffle(equipes_cadastradas)
        num_equipes = len(equipes_cadastradas)
        
        with open("chaves.txt", "w", encoding="utf-8") as chvs:
            for i in range(0, num_equipes, self.tam_chave):
                chave = f"Chave {i // self.tam_chave + 1}: {' | '.join(equipes_cadastradas[i:i+self.tam_chave])}\n"
                chvs.write(chave)
                print(chave)

class jogos(chave):
    def __init__(self, chaves):
        self.chaves = chaves
        
    def gerar_jogos(self):
        sorteio_jogos = []
        with open(self.chaves, "r", encoding="utf-8") as jogos:
            conteudo = jogos.read()
            linhas = conteudo.splitlines()
            for linha in linhas:
                palavras = linha.split(":")
                jogos_equipe = palavras[1].split("|")
                sorteio_jogos.extend(jogos_equipe)  # Use extend para adicionar as equipes individuais

        # Embaralha as equipes
        random.shuffle(sorteio_jogos)

        # Divide as equipes em jogos e escreve no arquivo "jogos.txt"
        num = len(sorteio_jogos)
        tam = 2
        with open("jogos.txt", "w", encoding="utf-8") as jgs:
            for i in range(0, num, tam):
                equipes_do_jogo = sorteio_jogos[i:i+tam]
                jogo = f"Jogo {i // tam + 1}: {' vs '.join(equipes_do_jogo)}\n"
                jgs.write(jogo)
                print(jogo)

  
    def exibir_jogos(self):
        pass


class gerenciar_cadastro_aluno(Aluno):
    def __init__(self, nome, curso, turma):
        super().__init__(nome, curso, turma)

    def editar_aluno(self, novo_nome, novo_curso, nova_turma):
        self.set_nome(novo_nome)
        self.curso = novo_curso  # Note que 'curso' é um atributo público
        self.set_turma(nova_turma)
    def excluir_aluno(self):
        pass
    def exibir_edicoes(self):
        pass





