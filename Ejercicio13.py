# Los parametros numericos se comportan de forma similar al paso por valor porque son inmutables; las funciones usan variables locales y el procedimiento solo muestra resultados.
def solicitar_compra(numero):
	print("Compra", numero)
	producto = input("Producto: ")
	precio = float(input("Precio: C$ "))
	cantidad = int(input("Cantidad: "))
	return producto, precio, cantidad


def calcular_subtotal(precio, cantidad):
	subtotal = precio * cantidad
	return subtotal


def calcular_descuento(subtotal):
	descuento = 0
	if subtotal >= 3000:
		descuento = subtotal * 0.08
	return descuento


def calcular_iva(monto):
	iva = monto * 0.15
	return iva


def mostrar_resumen(producto, subtotal, descuento, iva, total):
	print("--- RESUMEN DE COMPRA ---")
	print("Producto:", producto)
	print("Subtotal: C$", round(subtotal, 2))
	print("Descuento: C$", round(descuento, 2))
	print("IVA: C$", round(iva, 2))
	print("Total: C$", round(total, 2))


for numero_compra in range(1, 3):
	producto, precio, cantidad = solicitar_compra(numero_compra)
	subtotal = calcular_subtotal(precio, cantidad)
	descuento = calcular_descuento(subtotal)
	monto_con_descuento = subtotal - descuento
	iva = calcular_iva(monto_con_descuento)
	total = monto_con_descuento + iva
	mostrar_resumen(producto, subtotal, descuento, iva, total)