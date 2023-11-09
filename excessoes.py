class nomeException(Exception):
    pass
class opcaoException(Exception):
    pass
def option(opcao, x, y):
   if opcao > x or opcao < y :
       raise opcaoException