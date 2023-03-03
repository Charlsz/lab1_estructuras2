from arbol import *
from archivo import *

avl = AVL()
arbol = procesar_archivo_csv('punto1/User_track_data.csv') #Aqui empieza el error
'''
for lista in resultado:
    print(lista)
    clave = lista[0]
    valor = lista[1:]
    avl.insertar(avl.raiz, (clave, valor))
'''

avl.inorden(arbol)
