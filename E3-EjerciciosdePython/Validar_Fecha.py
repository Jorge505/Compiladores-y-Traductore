import re

print("Introduce cada valor que se tepida en entero empj: 2021/05/13")

agno= input("Introduce el año: ")
mes= input("Introduce el mes: ")
dia= input("Introduce el dia: ")

fecha= f"{agno}/{mes}/{dia}"
def fecha_valida(cadena):
  patron='^20[0-9]{2}/(0\d|1[0-2])/(0\d|1[0-9]|2[0-9]|3[0-1]$)'

  return bool(re.search(patron, cadena))

print(fecha_valida(fecha))