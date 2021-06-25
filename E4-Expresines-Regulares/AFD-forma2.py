import re

print("Ingresa la expresion regular del automata en binarios pares")
texto = input()
mat = re.search("(0|1)*011", texto)

if mat:
    print("Expresión válida ✔️")
else:
    print("Expresión invalida ❌")