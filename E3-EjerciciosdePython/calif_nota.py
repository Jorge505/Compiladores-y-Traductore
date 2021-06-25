
'''Ejercicio_11

Si deseas leer las calificaciones de una clase de infotmatica 
y contar el numero de aprobados (5 o mayor que 5)'''


print("--Programa para leer las calificaciones de una clase de informatica--")
print("")

print("Introduce el valor segun la clase a elegir")

print("0.Seguridad informatica \n1.Programacion_1 \n2.Compiladores y Traductores \n3.Administracion de Redes")
elegir = int(input("Introduce el valor aqui: "))

myLista = ["Seguridad informatica","Programacion 1","Compiladores y Traductores","Administracion de Redes"]

print("")
print("")
print("--- La clase elegida fue: " + myLista[elegir])
print("")
print("")

nota_Es = int(input("Ingrese el numero de estudiante: "))

cont = 1
apro=0
while cont <= nota_Es:
	print(f"Ingrese la nota del {cont} estudiante: ")
	nota = int(input("Nota: "))
	

	if nota >= 5:
		apro += 1

	cont = cont+1
	
print(f"La cantidad de estudiantes aprobado es {apro}")

