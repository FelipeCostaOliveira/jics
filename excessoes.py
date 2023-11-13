class nomeException(Exception):
    pass
class opcaoException(Exception):
    pass
class matriculaException(Exception):
    pass

def option(opcao, x, y):
   if opcao > x or opcao < y :
       raise opcaoException
   
def name(nome):
    if not nome.replace(" ", "").isalpha():
         raise nomeException
    
def mat(matricula, n):
    if matricula.isdigit() and len(matricula) >= n:
        pass
    else:
        raise matriculaException
        