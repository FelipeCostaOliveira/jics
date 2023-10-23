import os, sys
import random
import itertools
from datetime import datetime, timedelta
import funcoes


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
    

class Professor(Pessoa):
    def __init__(self, nome, matricula, senha):
        super().__init__(nome, matricula)
        self.__senha = senha

        def get_senha(self):
          return self.__senha

        def set_senha(self, nova_senha):
          self.__senha = nova_senha
          
    def cad_professor(self, senha): 
      funcoes.gerar_dir("Arquivos") 
      caminho = os.path.join("Arquivos", "Professores_cadastrados.txt")     
      with open(caminho, "a", encoding="utf-8") as arquivo :
        # Escrever os dados do professor no arquivo
        arquivo.write(f" Nome: {self.get_nome()}, Número Matrícula: {self.get_matricula()}, Senha: {senha}\n")


class Chave:
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
                        if len(linhas) < 3:
                            break
                        for linha in linhas:
                            if "Curso:" in linha:
                                palavras = linha.split()  # Dividir a linha em palavras
                                indice_curso = palavras.index("Curso:")
                                curso = palavras[indice_curso + 1]
                                turma = palavras[indice_curso + 3]
                                Equipe = f"{curso}-{turma}"
                                if Equipe in equipes_cadastradas:
                                    break
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


class Jogos:
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
            for chave in chaves:
                equipes_chave = sorteio_jogos[chave]
                num_equipes = len(equipes_chave)

                for i in range(num_equipes):
                    for j in range(i + 1, num_equipes):
                        equipe1 = equipes_chave[i]
                        equipe2 = equipes_chave[j]
                        inicio_formatado = self.inicio.strftime(formato_brasil)
                        termino = self.inicio + timedelta(minutes=30)
                        termino_formatado = termino.strftime(formato_brasil)
                        jogo = f"{chave}: {equipe1} vs {equipe2} | Início: {inicio_formatado} Término: {termino_formatado}\n"
                        jgs.write(jogo)
                        self.inicio = termino + timedelta(minutes=5)
                        if chave not in self.jogos:
                            self.jogos[chave] = []
                        self.jogos[chave].append(jogo)
        funcoes.organizar_horarios()


class GerenciarCadastroAluno:
    def __init__(self, matricula):
        self.matricula = matricula

    def editar_aluno(self):

        cursos = {
            "1": "Informática",
            "2": "Eletrotécnica",
            "3": "Química",
            "4": "Edificações"
        }
        turmas = {
            "1": "1°A",
            "2": "1°B",
            "3": "2°Mat",
            "4": "2°Vesp",
            "5": "3°Mat",
            "6": "3°Vesp"
        }

        caminho_diretorio = os.getcwd()
        nome_atual = ""
        matricula_atual = ""
        curso_atual = ""
        turma_atual = ""

        for pasta, _, arquivos in os.walk(caminho_diretorio):
            for arquivo in arquivos:
                if arquivo in ["professores_cadastrados.txt", "jogos.txt", "chaves.txt"]:
                    continue
                if arquivo.endswith(".txt"):
                    caminho_arquivo = os.path.join(pasta, arquivo)
                    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_txt:
                        for linha in arquivo_txt:
                            partes = linha.split(":")
                            if len(partes) < 3:
                                continue
                            matricula_na_linha = partes[2].replace(", Curso", "").strip()
                            if matricula_na_linha == self.matricula:
                                nome_atual = partes[1].replace(", Número Matrícula", "").strip()
                                matricula_atual = linha.split(":")[2].replace(", Curso", "").strip()
                                curso_atual = linha.split(":")[3].replace(" Turma", "").strip()
                                turma_atual = linha.split(":")[4].strip()
                                print(
                                    f"nome= {nome_atual} matricula= {matricula_atual} "
                                    f"curso= {curso_atual} turma= {turma_atual}")
        self.excluir_aluno()
        novo_nome = nome_atual
        nova_matricula = matricula_atual
        sala = curso_atual
        serie = turma_atual
        trocar_nome = int(input("Deseja trocar o nome? (digite 1 p/sim ou 2 p/não)"))
        if trocar_nome == 1:
            novo_nome = input("Digite o novo nome: ")
            while not novo_nome.replace(" ", "").isalpha():
                print("\033[31mnome inválido digite apenas letras ou espaços\033[0m")
                novo_nome = input("Digite o nome: ").capitalize().strip()

        trocar_matricula = int(input("Deseja trocar a matrícula? (digite 1 p/sim ou 2 p/não)"))
        if trocar_matricula == 1:
            nova_matricula = input("Digite a nova matricula: ")
            while True:
                if nova_matricula.isdigit() and len(nova_matricula) >= 10:
                    break
                else:
                    print(f"\033[31mMatrícula inválida, digite apenas números com no mínimo 10 algarismos.\033[0m")
                    nova_matricula = input("Digite a matrícula: \n ")
        trocar_curso = int(input("Deseja trocar o curso? (digite 1 p/sim ou 2 p/não)"))
        if trocar_curso == 1:
            print("\nCursos disponíveis:")
            for key, value in cursos.items():
                print(f"{key} - {value}")
            novo_curso = input("\nDigite o número correspondente ao curso do discente: ").capitalize()
            sala = cursos[novo_curso]
        trocar_turma = int(input("Deseja trocar a turma? (digite 1 p/sim ou 2 p/não)"))
        if trocar_turma == 1:
            print("\nTurmas disponíveis:")
            for key, value in turmas.items():
                print(f"{key} - {value}")
            nova_turma = input("Digite o número correspondente à turma do discente: ").capitalize()
            serie = turmas[nova_turma]

        pessoa = Aluno(novo_nome, nova_matricula, sala, serie)
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
                            if len(linha.split(":")) < 3:
                                continue
                            total = linha.split(":")[2].replace(", Curso", "").strip()

                            if total != self.matricula:
                                linhas_filtradas.append(linha)

                    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo_txt:
                        arquivo_txt.writelines(linhas_filtradas)
