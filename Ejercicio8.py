#Es correcto: modificar una lista dentro de una funcion afecta la variable exterior. 
def agregar_producto(inventario, producto):
	inventario.append(producto)


productos = ["arroz", "aceite"]
agregar_producto(productos, "cafe")

print(productos)
