class Nodo:
    """
    esta clase representa un nodo en un arbol avl
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class AVL:
    def insertar(self, raiz, valor):
        """
        aqui insertamos un nuevo nodo buscando la ubicacion correcta
        de este en el arbol y luego actualiza las alturas
        de todos los nodos y realiza las rotaciones necesarias para mantener el arbol balanceado
        """
        if not raiz:
            return Nodo(valor)
        elif valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)
        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda),
                              self.obtener_altura(raiz.derecha))
        balance = self.obtener_balance(raiz)
        if balance > 1 and valor < raiz.izquierda.valor:
            return self.rotar_derecha(raiz)
        if balance < -1 and valor > raiz.derecha.valor:
            return self.rotar_izquierda(raiz)
        if balance > 1 and valor > raiz.izquierda.valor:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        if balance < -1 and valor < raiz.derecha.valor:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)
        return raiz

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        """
        este metodo funciona para obtener la diferencia de altura entre los
        subarboles izquiero y derecho de un nodo
        """
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotar_derecha(self, z):
        y = z.izquierda
        t3 = y.derecha
        y.derecha = z
        z.izquierda = t3
        z.altura = 1 + max(self.obtener_altura(z.izquierda),
                           self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda),
                           self.obtener_altura(y.derecha))
        return y

    def rotar_izquierda(self, z):
        y = z.derecha
        t2 = y.izquierda
        y.izquierda = z
        z.derecha = t2
        z.altura = 1 + max(self.obtener_altura(z.izquierda),
                           self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda),
                           self.obtener_altura(y.derecha))
        return y

    def imprimir_arbol(self, raiz, espacio):
        """
        se utiliza para imprimir en arbol en orden de recorrido Inorden
        imprime los nodos del subarbol derecho antes que los del subarbol izquiero. asi para reflejar
        el hecho de que los valores mas grandes se encuentran en el subarbol derecho del arbol BST (binary search tree)
        """
        if not raiz:
            return
        espacio += 10
        self.imprimir_arbol(raiz.derecha, espacio)
        print(end='\n')
        for i in range(10, espacio):
            print(end=' ')
        print(raiz.valor)
