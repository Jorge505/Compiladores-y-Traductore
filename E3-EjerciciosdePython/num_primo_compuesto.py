'''21-Dado un entero positivo n (>1)
 comprobar si es primo o compuesto'''

n = int(input("Ingresa un numero: "))

div = 2
while n > div:
    if n%div == 0:
        print("Es compuesto")
        break

    elif n%div != 0:
        div=div+1

if n == div:
    print("Es un numero primo")