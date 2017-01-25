#Ejercicio Tablas de Multiplicar

numeros = list(range(11))

for variable in numeros:
	print(" ")
	print("Tabla del"),(variable)
	print("-----------")
	for n in numeros:
		print(variable),("*"), (numeros[n]), ("es"), (variable*numeros[n])

				

