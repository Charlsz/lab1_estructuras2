import csv

def letra_a_numero(letra):
    if letra.isalpha():
        return ord(letra.lower()) - 96
    else:
        return letra

def procesar_archivo_csv(archivo):
    lineas = []
    with open(archivo) as csv_file:
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
    
    resultado = []
    for clave, grupo in grupos.items():
        lista_resultado = grupo[0]
        for linea in grupo[1:]:
            lista_resultado[2:5] += linea[2:5]
        resultado.append(lista_resultado)
    
    for i, lista in enumerate(resultado):
        nombre_variable = ''.join([str(letra_a_numero(letra)) for letra in lista[1]])
        exec(f"var{i+1} = {lista}")
    
    for i in range(len(resultado)):
        nombre_variable = f"var{i+1}"
        print(nombre_variable + ": " + str(eval(nombre_variable)))
    
    return resultado
