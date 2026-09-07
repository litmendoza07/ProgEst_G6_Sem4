 # Reasignar el parametro dentro de la funcion no cambia la variable original y el cambio se observa fuera de la funcion.
def aumentar_salario(salario):
	salario += 100
	print("Salario dentro:", salario)


salario_original = 1000
aumentar_salario(salario_original)
print("Salario fuera:", salario_original)


def agregar_venta(ventas, nueva_venta):
	ventas.append(nueva_venta)


ventas_registradas = [500, 800]
agregar_venta(ventas_registradas, 1200)
print("Ventas fuera:", ventas_registradas)
