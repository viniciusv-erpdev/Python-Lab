
tipos_acidentes = [
    "Colisão",
    "Atropelamento",
    "Colisão",
    "Queda",
    "Colisão",
    "Atropelamento",
    "Queda",
    "Colisão"
]

def contar_ocorrencias(acidentes, parametro_ocorrencias):

    acidentes_enumerados = {}
    minimo_ocorrencias = {}

    for acidente in acidentes:

        if acidente not in acidentes_enumerados:
        
            acidentes_enumerados[acidente] = 1

        else:

            acidentes_enumerados[acidente] += 1

    for acidente, contagem in acidentes_enumerados.items():

        if contagem == parametro_ocorrencias:

            minimo_ocorrencias[acidente] = contagem

    return minimo_ocorrencias

print(contar_ocorrencias(tipos_acidentes, 4))