# Es correcto: El procedimiento realiza una accion con print y no devuelve un resultado mediante return.
def mostrar_resumen(cliente, total):
	print("--- RESUMEN DE VENTA ---")
	print("Cliente:", cliente)
	print("Total: C$", total)


mostrar_resumen("Ana Lopez", 136.50)
