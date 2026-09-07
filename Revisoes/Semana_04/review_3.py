# Criar uma lista de notas em formato de letras a partir de um limite de notas

highest = 88

def letter_grades(highest):

    list_of_notes = [41]

    evenly_increment = (highest - 40)/4

    for i in range(3):

        note = list_of_notes[i] + evenly_increment
        list_of_notes.append(note)

    return list_of_notes

print(letter_grades(highest))