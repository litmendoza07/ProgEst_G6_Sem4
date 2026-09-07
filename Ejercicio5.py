# Una variable global puede usarse dentro de una funcion, una local solo existe en su funcion y global permite modificar un dato externo.
nombre_empresa = "TecnoVentas"


def mostrar_empresa():
	print(nombre_empresa)


mostrar_empresa()


def crear_total():
	total = 2500
	return total


crear_total()

try:
	print(total)
except NameError:
	print("Error: total solo existe dentro de crear_total")


contador = 0


def incrementar_contador():
	global contador
	contador += 1


incrementar_contador()
incrementar_contador()
print("Contador:", contador)
