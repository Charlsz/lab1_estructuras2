from arbol import *
from archivo import *

avl = AVL()
resultado = procesar_archivo_csv('punto1/User_track_data.csv')

for lista in resultado:
    clave = lista[0]
    valor = lista[1:]
    avl.insertar(avl.raiz, (clave, valor))

AVL.inorden(avl.raiz)
