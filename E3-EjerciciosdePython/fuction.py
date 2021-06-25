'''26-Diseñar una funcion que calcule x^n
 para x variable real y para n variable entera
'''

def calculando():
	x = float(input("Ingrese la base de x= "))
	n = int(input("Ingrese el valor exponecial de n= "))

	return x**n

print(f"El resultado de su potencia es de:  {calculando()}")