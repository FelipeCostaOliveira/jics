import cadastro
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
    # elif exclusivo para teste
    elif quem == 3:
        pass
    elif quem == 4:
        pass
  except ValueError:
    print("\033[031mdigite somente números\033[0m")
  
  