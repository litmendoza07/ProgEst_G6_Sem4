def clasificar_nota(note):
    if note < 1 or note > 100:
        return "Nota inválida"
    if note < 60:
        return "Aprendizaje inicial"
    if note < 70:
        return "Aprendizaje fundamental"
    if note < 90:
        return "Aprendizaje satisfactorio"
    return "Aprendizaje avanzado"


def clasificar_notas(notes):
    return [(note, clasificar_nota(note)) for note in notes]
