from arbol import *
arbol = AVL()
raiz = None
#creamos el arbol que mostramos al inicio de toprueba2.txt
raiz = arbol.insertar(raiz, 30)
raiz = arbol.insertar(raiz, 20)
raiz = arbol.insertar(raiz, 40)
raiz = arbol.insertar(raiz, 10)
raiz = arbol.insertar(raiz, 25)
raiz = arbol.insertar(raiz, 50)
#arbol.inorden(raiz)

#insertaremos el valor de 15 y veremos que realiza automaticamente la rotación para que se autobalanceé
raiz = arbol.insertar(raiz, 15)
arbol.inorden(raiz)




