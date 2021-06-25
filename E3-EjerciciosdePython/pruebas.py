nom = input("Ingresa tu nombre: ")

est = int(input("Introduce la cantidad de nota a calcular: "))

prom = 0
for cont in range(1,est+1):
	nota = int(input(f"Digite la nota_{cont} del estudiante: "))
	prom = prom + nota

print(f"{nom} tu promedio es de {prom/est}")
