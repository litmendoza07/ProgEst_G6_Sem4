# Se mantuvo `saldo = 5000` como variable global y se creó otro `saldo = 1200` dentro de `mostrar_saldo()`. La variable local solo existe dentro de la función, por eso primero se muestra `1200` y después `5000`, demostrando que la variable global no fue modificada.
saldo = 5000


def mostrar_saldo():
	saldo = 1200
	print(saldo)


mostrar_saldo()
print(saldo)
