
numero = 5

if numero > 0:
    print("El numero es positivo")

if numero < 0:
    print("El numero es negativo")

if numero == 0:
    print("El numero es nulo")


if numero > 0:
    if numero >= 10 and numero <= 99:
        print("El numero es positivo y tiene dos digitos")
    else:
        print("El numero es positivo y no tiene dos digitos")
else:
    if numero >= -999 and numero <= -100:
        print("El numero es negativo y tiene tres digitos")
    else:
        print("El numero es negativo y no tiene tres digitos")