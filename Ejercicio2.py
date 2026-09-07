# Se eliminó global y el contador se actualiza con parámetros y retorno.
def registrar_venta(ventas_registradas):
	ventas_registradas += 1
	print("Venta registrada")
	return ventas_registradas


ventas_registradas = 0
ventas_registradas = registrar_venta(ventas_registradas)
ventas_registradas = registrar_venta(ventas_registradas)

print("Total de ventas:", ventas_registradas)

