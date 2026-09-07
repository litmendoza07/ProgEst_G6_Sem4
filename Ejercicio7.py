#Es correcto: reasignar un parámetro dentro de la función no modifica la variable exterior.
def aplicar_aumento(precio):
    precio = precio + 100
    print("Precio dentro:", precio)


precio_producto = 500
aplicar_aumento(precio_producto)

print("Precio fuera:", precio_producto)