import numpy as np

def generarResultados(datos: list) -> dict:

    ajustados = []

    for part in datos:
        part = list(map(lambda puntaje: 3 if puntaje < 4 else puntaje, part))
        ajustados.append(part)

    matriz = np.array(ajustados)
    promedio = round(matriz.mean(), 2)
    calificacion = np.sum(matriz, axis = 1)
    ganador = calificacion.argmax() + 1

    final = {
            'puntaje promedio': promedio,
            'puntaje participante 1': calificacion[0],
            'puntaje participante 2': calificacion[1],
            'puntaje participante 3': calificacion[2],
            'participante ganador' : ganador
    }
    return final

print(generarResultados([[2,5,4], [7,6,5], [9,7,5]]))
print(generarResultados([[7,3,5], [2,2,3], [4,2,5]]))