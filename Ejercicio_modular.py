# El siguiente ejercicio pide leer n cantidad de notas, decir si es aprendizaje incial, fundamental, satisfactorio, avanzado y muestra todas las notas.
def clasificar_nota(note):
    if 1 <= note <= 59:
        return "Aprendizaje inicial"
    elif 60 <= note <= 69:
        return "Aprendizaje fundamental"
    elif 70 <= note <= 89:
        return "Aprendizaje satisfactorio"
    elif 90 <= note <= 100:
        return "Aprendizaje avanzado"
    else:
        return "Nota inválida"


def programa():
    notes = []
    cantidad = int(input("¿Cuántas notas desea ingresar? "))

    for i in range(cantidad):
        note = float(input(f"Ingrese la nota {i + 1} (1-100): "))
        notes.append(note)

    print("\nTodas las notas:")
    for note in notes:
        print(f"{note} - {clasificar_nota(note)}")

programa()