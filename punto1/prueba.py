from arbol import *
from archivo import *
arbol = AVL()
raiz = None

procesar_archivo_csv('User_trac_data.csv')

raiz = arbol.insertar(raiz, 30)
arbol.inorden(raiz)