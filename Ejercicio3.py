# Calcular_iva se movió al nivel principal para reutilizarse fuera de procesar_venta.
def calcular_iva(subtotal):
	return subtotal * 0.15


def procesar_venta(subtotal):
	iva = calcular_iva(subtotal)
	return subtotal + iva


total = procesar_venta(2000)
print("Total: C$", total)
