PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6
# constantes que representan las diferentes piezas de ajedrez:
class Node:
    def __init__(self, board, moves):
        self.board = board
        self.moves = moves
        self.children = []
#Cada nodo tiene un tablero de ajedrez (board) y una lista de movimientos posibles (moves) en ese tablero, así como una lista de nodos hijo (children) que representan los movimientos posibles siguientes.        

class ChessTree:
    def __init__(self, board):
        self.root = Node(board, None)
#se inicializa con un nodo raíz (root) que representa el tablero de ajedrez actual.        

def generate_tree(self, node, depth):
    if depth == 0:
        return
    for move in node.moves:
        new_board = make_move(node.board, move)
        new_moves = generate_moves(new_board)
        child = Node(new_board, new_moves)
        node.children.append(child)
        self.generate_tree(child, depth - 1)
"""
El método generate_tree utiliza la recursión para generar el árbol de decisión. Dado un nodo node y una profundidad depth, el método genera los nodos hijo correspondientes a partir de los movimientos posibles en el tablero de ajedrez del nodo actual. Para cada movimiento posible (move), se crea un nuevo tablero de ajedrez (new_board) y una nueva lista de movimientos posibles (new_moves) en ese tablero. 



"""        


def evaluate_board(self, board):
    score = 0
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece == PAWN:
                score += 1
            elif piece == KNIGHT or piece == BISHOP:
                score += 3
            elif piece == ROOK:
                score += 5
            elif piece == QUEEN:
                score += 9
            elif piece == KING:
                score += 100
    return score

#recorre todas las celdas del tablero de ajedrez (board) y suma un puntaje (score) para cada pieza de ajedrez.
#  Las puntuaciones se asignan en función delvalor relativo de cada pieza, donde el peón vale 1 punto, el caballo y el alfil valen 3 puntos, la torre vale 5 puntos, la reina vale 9 puntos y el rey vale 100 puntos.
def find_best_move(self, depth):
    self.generate_tree(self.root, depth)
    best_score = float('-inf')
    best_move = None
    for child in self.root.children:
        score = self.evaluate_board(child.board)
        if score > best_score:
            best_score = score
            best_move = child.moves[0]
    return best_move
""""El método find_best_move llama al método generate_tree para generar el árbol de decisión con una profundidad dada (depth). A continuación, evalúa todos los nodos hijo del nodo raíz (self.root.children) y encuentra el puntaje más alto (best_score) y el movimiento correspondiente (best_move). Finalmente, devuelve el mejor movimiento.

"""