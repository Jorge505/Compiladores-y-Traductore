''' 	21-Imprima una tabla de multiplicar como
      1   2  3  4  ...  15
 **  **  **  ** ** **   **
 1*   1   2  3  4  ...  15
 2*   2   4  6  8  ...  30 
 3*   3   6  9  12 ...  45
 .
 .
 15*  15  30  45  60 ... 225'''

for fila in range(1,16):
	for column in range(1,16):
		print(fila*column, end="\t")
	print("")


