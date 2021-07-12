import math

def calcularDistancia(c1: str, x1: int, y1: int, c2: str, x2: int, y2: int) -> str:


    distancia = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2),2)
    return "La distancia entre las ciudades {} y {} es de {} kilómetros ".format(c1, c2, distancia)

print(calcularDistancia("Pereira", 5, 50, "Ibague", 55, 10))
print(calcularDistancia("Bogota", 12, 3, "Tunja", 16, 5))
print(calcularDistancia("Roma", 45, 50, "Venecia", 46, 60))
print(calcularDistancia("Berlin", 50, 70, "Munich", 50, 60))
    