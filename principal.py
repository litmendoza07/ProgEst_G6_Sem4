import notas

def pedir_notas():
    cantidad = int(input("¿Cuántas notas desea ingresar? "))
    lista_notas = []

    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        lista_notas.append(nota)

    return lista_notas


def mostrar_notas(lista_notas):
    if not lista_notas:
        print("\nNo hay notas ingresadas.")
        return

    notas_clasificadas = notas.clasificar_notas(lista_notas)

    print("\nNotas ingresadas:")
    for nota, clasificacion in notas_clasificadas:
        print(f"Nota: {nota} - {clasificacion}")


def menu():
    lista_notas = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Ingresar notas")
        print("2. Mostrar notas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista_notas = pedir_notas()
        elif opcion == "2":
            mostrar_notas(lista_notas)
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


menu()