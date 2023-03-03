import csv
from arbol import *
def letra_a_numero(letra):
    if letra.isalpha():
        return ord(letra.lower()) - 96
    else:
        return letra

def procesar_archivo_csv(archivo):
    lineas = []
    with open(archivo, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for linea in csv_reader:
            lineas.append(linea)

    grupos = {}
    for linea in lineas:
        clave = (linea[0], linea[1])
        if clave not in grupos:
            grupos[clave] = [linea]
        else:
            grupos[clave].append(linea)
            
    variables = {} # Crear un diccionario para almacenar las variables
    for i, (clave, grupo) in enumerate(grupos.items()):
        lista_resultado = grupo[0]
        for linea in grupo[1:]:
            lista_resultado[2:5] += linea[2:5]
        nombre_variable = ''.join([str(letra_a_numero(letra)) for letra in lista_resultado[1]]) #Transforma el ID del usuario a números
        variables[nombre_variable] = lista_resultado # Agregar cada variable al diccionario
    
    arbol = AVL()   # Crear el árbol AVL
    raiz = None

    
    for nombre_variable, lista in variables.items():
        raiz = arbol.insertarUsuario(raiz, nombre_variable, lista) # Agregar cada variable al nodo correspondiente del árbol

    return raiz # Devolver el árbol AVL resultante

