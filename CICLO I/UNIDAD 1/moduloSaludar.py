
def saludo(cadena):
    return "Hola {}! ¿cómo estas?".format(cadena)

el_saludo = saludo("Juan")
print(el_saludo)

import math

def calcularDistancia(c1: str, x1: int, y1: int, c2: str, x2: int, y2: int):

    c1 = "Pereira"
    x1 = 5
    y1 = 50
    c2 = "Ibague"
    x2 = 55
    y2 = 10

    distancia = "{0:.2f}".format(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    return "La distancia entre las ciudades {} y {} es de {} kilometros".format(c1, x1, y1, c2, x2, y2)

el_caldulo = calcularDistancia()
print(el_caldulo)
   
