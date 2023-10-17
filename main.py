from Classes import *
import cadastro
#import time
# from funcoes import *
# from gerar_chaveamento import equipes
#import random
from datetime import datetime, timedelta


'''frase = "\033[3;0;97m\n        Avaliação Prática -  Programação Orientada a Objetos(POO)\n                   2º ANO - Informática - Matutino\n\n                            Grupo Valhalla\n\nDocente:\n -> Camila Serrão\n\nDiscentes:\n -> Deny Willian de Lima Martins\n -> Felipe Costa de Oliveira \n -> Renan Neponuceno Barroso\n -> Stefano Gabriel Mendonça de Oliveira\n"


for i in frase:
  time.sleep(0.000001)
  print(i,end='', flush=True)
print()'''

print("Quem deseja acessar?")

while True:
  try:
    quem = int(input("1 - Aluno que irá cadastrar\n2 - Professores\n"))

    if quem == 1:
        cadastro.cadastro()
        break
    elif quem == 2:
        cadastro.acoes()
        break
    #elif exclusivo para teste
    elif quem == 3:
      caminho_raiz = os.getcwd()
      tamanho = 4
      sistem = chave(caminho_raiz, tamanho)
      sistem.gerar_chave()
      break

    elif quem == 4:
      arquivo = "Arquivos/chaves.txt"
      #path_jogos = "Arquivos/jogos.txt"
      inicio = datetime(2023, 11, 13, 10, 0)
      sortear = jogos(arquivo, inicio)
      sortear.gerar_jogos()
      sortear.exibir_jogos()
      break
    elif quem == 5:
      cadastro.editar_aluno()

        
  except ValueError:
    print("\033[031mdigite somente números\033[0m")
  
  