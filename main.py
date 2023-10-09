from Classes import *
import cadastro
import time
from registro import *
from gerar_chaveamento import equipes
import random
from datetime import datetime, timedelta


'''frase = "\033[3;0;97m\n        Avaliação Prática -  Programação Orientada a Objetos(POO)\n                   2º ANO - Informática - Matutino\n\n                            Grupo Valhalla\n\nDocente:\n -> Camila Serrão\n\nDiscentes:\n -> Deny Willian de Lima Martins\n -> Felipe Costa de Oliveira \n -> Renan Neponuceno Barroso\n -> Stefano Gabriel Mendonça de Oliveira\n"


for i in frase:
  time.sleep(0.000001)
  print(i,end='', flush=True)
print()'''

print("Quem deseja acessar?")
while True:
  quem = int(input("1 - Aluno que irá cadastrar\n2 - Professores\n"))

  if quem == 1:
      cadastro.cadastro()
      
      break
  elif quem == 2:
      cadastro.cadastro_professor()
      print("\nAlunos cadastrados: ")
      
      caminho_diretorio = os.getcwd()
      for pasta, _, arquivos in os.walk(caminho_diretorio):
        for arquivo in arquivos:
            if arquivo == "professores_cadastrados.txt":
              continue
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(pasta, arquivo)
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_txt:
                    conteudo = arquivo_txt.read()
                    lines = conteudo.splitlines()
                    for linha in lines:
                      parte = linha.split(", Curso")
                      parte_mantida = parte[0]
                      print(parte_mantida)
      break
  #elif exclusivo para teste
  elif quem == 3:
    caminho_raiz = os.getcwd()
    tamanho = 4
    sistem = chave(caminho_raiz, tamanho)
    sistem.gerar_chave()
    break

  elif quem == 4:
    arquivo = "chaves.txt"
    inicio = datetime(2023, 11, 13, 10, 0)
    sortear = jogos(arquivo, inicio)
    sortear.gerar_jogos()
    sortear.exibir_jogos()
    break
                  
          
   
        
      

  
