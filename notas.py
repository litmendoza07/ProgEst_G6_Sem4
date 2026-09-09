# El siguiente ejercicio pide leer n cantidad de notas, decir si es aprendizaje incial, fundamental, satisfactorio, avanzado y muestra todas las notas.
def classify_note(note):
    if note < 1 or note > 100:
        return "Nota inválida"
    if note < 60:
        return "Aprendizaje inicial"
    if note < 70:
        return "Aprendizaje fundamental"
    if note < 90:
        return "Aprendizaje satisfactorio"
    return "Aprendizaje avanzado"


def classify_notes(notes):
    return [(note, classify_note(note)) for note in notes]
