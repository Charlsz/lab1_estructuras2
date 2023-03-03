class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t):
        self.root = Node(leaf=True)
        self.t = t

    def insert(self, k):
        r = self.root  # Comienza la búsqueda de la ubicación de inserción en la raíz del árbol
        if len(r.keys) == (2*self.t) - 1:  # Si la raíz está llena, se necesita una nueva raíz
            s = Node()
            self.root = s
            s.child.insert(0, r)   # Mueve la antigua raíz a ser el primer hijo de la nueva raíz
            self._split_child(s, 0)  # Divide el primer hijo de la nueva raíz y ajusta los punteros de los nodos
            self._insert_non_full(s, k)  # Llama al método _insert_non_full para insertar la clave en el árbol
        else:
            self._insert_non_full(r, k)  # Si la raíz no está llena, llama directamente a _insert_non_full

    def _insert_non_full(self, x, k):
  
        i = len(x.keys) - 1  # Comienza la búsqueda de la ubicación de inserción en el nodo `x`
        if x.leaf:  # Si `x` es una hoja, simplemente inserta la clave en el lugar correcto
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:  # Si `x` es un nodo interno, busca el hijo adecuado y llama recursivamente a _insert_non_full en ese hijo
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2*self.t) - 1:  # Si el hijo está lleno, lo divide y ajusta los punteros de los nodos
                self._split_child(x, i)
                if k > x.keys[i]:  # Determina el hijo adecuado después de la división del nodo hijo
                    i += 1
            self._insert_non_full(x.child[i], k)  # Llama recursivamente a _insert_non_full en el hijo adecuado


    def _split_child(self, x, i):
        t = self.t
        y = x.child[i]  # El nodo hijo a dividir
        z = Node(leaf=y.leaf)  # Crea un nuevo nodo para almacenar las claves más grandes de `y`
        x.child.insert(i+1, z)  # Inserta el nuevo nodo como hermano del nodo `y`
        x.keys.insert(i, y.keys[t-1])  # Mueve la clave central de `y` al nodo `x`
        z.keys = y.keys[t:(2*t-1)]  # Copia las claves más grandes de `y` al nuevo nodo `z`
        y.keys = y.keys[0:(t-1)]  # Actualiza la lista de claves de `y` para que contenga solo las claves más pequeñas
        if not y.leaf:  # Si `y` no es una hoja, también hay que copiar sus hijos correspondientes
            z.child = y.child[t:(2*t)]
            y.child = y.child[0:(t-1)]

    def search(self, k, x=None):
        if isinstance(x, Node):  # Comprueba si se ha especificado un nodo inicial
            i = 0
            while i < len(x.keys) and k > x.keys[i]:  # Busca la posición de la clave en la lista de claves del nodo actual
                i += 1
            if i < len(x.keys) and k == x.keys[i]:  # Si se encuentra la clave, devuelve el nodo actual y el índice donde se encuentra la clave
                return (x, i)
            elif x.leaf:  # Si el nodo actual es una hoja y no se encuentra la clave, la clave no está en el árbol
                return None
            else:  # Si el nodo actual no es una hoja, sigue buscando en el hijo correspondiente
                return self.search(k, x.child[i])
        else:  # Si no se ha especificado un nodo inicial, comienza la búsqueda desde la raíz del árbol
            return self.search(k, self.root)


    def _print_recursive(self, x, verbose=False):
        if verbose:
            print(x.keys)
        if x.leaf:
            return str(x.keys)
        else:
            s = ''
            for i in range(len(x.keys)):
                child = self._print_recursive(x.child[i], verbose)
                s += child + str(x.keys[i]) + ', '
            s += self._print_recursive(x.child[len(x.keys)], verbose)
            return s
