# Definiendo tabla de transiciones
tabla = [[1,2], [3,0], [3,0], [None,4], [None,5], [None,None]]

# Obtener columna
def columna(simbolo):
    c = 0
    if simbolo == "1":
        c = 1
    if simbolo == "0":
        c = 0
    return c

# Obtener fila
def fila(estado):
    f = 0
    if estado == 0:
        f = 0
    if estado == 1:
        f = 1
    if estado == 2:
        f = 2
    if estado == 3:
        f = 3
    if estado == 4:
        f = 4
    if estado == 5:
        f = 5
    return f

# Función de transición
def mover(estado, simbolo):
    c = columna(simbolo)
    f = fila(estado)
    return tabla[f][c]

# Main
def main():

    # Variable implicadas
    i = 1
    print("Introduce numero de automata en binarios pares: ")
    cadena2 = input() #"0011\n"
    cadena = cadena2 + "\n"
    estado = 0
    simbolo = cadena[0]

    # Primera ejecución
    print("#" + " -> \t" + "Estado" + " \t" + "Simbolo")
    print(str(i) + " -> \t" + str(estado) + " \t" + str(simbolo))

    # El proceso se repite hasta el fin de línea
    while (str(simbolo) != '''\n'''):
        estado = mover(estado, simbolo)
        simbolo = cadena[i]
        i = i + 1
        print(str(i) + " -> \t" + str(estado) + " \t" + str(simbolo))
        
    if (estado == 5):
        print('Expresión válida ✔️')
    else:
        print('Expresión invalida ❌')

main()