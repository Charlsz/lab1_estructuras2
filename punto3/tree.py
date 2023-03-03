"""
Problema 
    Generar un codigo que permita insertar datos en una estructura de arbol la cual garantice que luego su busqueda sea la mas eficiente

"""
class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t): #t es el orden del arbol
        self.root = Node(leaf=True)
        self.t = t

    def insert(self, k):
        """
        Funcion para insertar llaves en el arbol
        """
        if self.root is None:
            self.root = Node(True)
            self.root.keys.append(k)
            return
            
        r = self.root 
        if len(r.keys) == (2*self.t) - 1:  # Si la raíz está llena, se necesita una nueva raíz
            s = Node()
            self.root = s
            s.child.insert(0, r)   # Mueve la antigua raíz a ser el primer hijo de la nueva raíz
            self._split_child(s, 0)  # Divide el primer hijo de la nueva raíz y ajusta los punteros de los nodos
            self._insert_non_full(s, k)  
        else:#En caso de que la raiz no este llena
            self._insert_non_full(r, k)  

    def _insert_non_full(self, x, k):
        """
        Funcion para insertrar datos en el nodo mientras tenga espacio
        """
  
        i = len(x.keys) - 1  # se inicializa un i con el maximo de datos que pueden ser almacenados en el nodo
        if x.leaf:  # Si el nodo es una hoja, simplemente inserta la clave en el lugar correcto
            x.keys.append(k)
            x.keys.sort()
        else:  # Si el nodo no es hoja, busca el hijo adecuado y llama recursivamente a _insert_non_full en ese hijo
            while i >= 0 and k < x.keys[i]:#ubica el dato en la posicion adecuada 
                i -= 1
            i += 1
            self._insert_non_full(x.child[i], k)  # Llama recursivamente a _insert_non_full en el hijo adecuado
            if len(x.child[i].keys) == (2*self.t) - 1:  # Si el hijo está lleno, lo divide y ajusta los punteros de los nodos
                self._split_child(x, i)
                if k > x.keys[i]:  # Determina el hijo adecuado después de la división del nodo hijo
                    i += 1
           

    def _split_child(self, x, i):
        """
        Funcion para dividir el nodo 
        """
        t = self.t
        y = x.child[i]  # El nodo hijo a dividir
        z = Node(leaf=y.leaf)  # Crea un nuevo nodo para almacenar los datos más grandes
        x.child.insert(i+1, z)  # Inserta el nuevo nodo al lado del 
        x.keys.insert(i, y.keys[t-1])  # Mueve la clave central
        z.keys = y.keys[t:(2*t-1)] 
        y.keys = y.keys[0:(t-1)]  # Actualiza la lista para que contenga solo las claves más pequeñas
        if not y.leaf:  # Si el nodo no es una hoja, también hay que copiar sus hijos correspondientes
            z.child = y.child[t:(2*t)]
            y.child = y.child[0:(t-1)]
  
    def print_tree(self, x, l=0):
        """
        Funcion para imprimir el arbol 
        Creditos to https://www.programiz.com/dsa/b-tree
        """
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

    
def main():
    #se crea el árbol
    B = BTree(2)
    #se insertan las llaves en el árbol
    B.insert(000)
    B.insert(111)
    B.insert(110)
    B.insert(101)


    #se imprime el árbol
    B.print_tree(B.root)
    
if __name__ == '__main__':
    main()
