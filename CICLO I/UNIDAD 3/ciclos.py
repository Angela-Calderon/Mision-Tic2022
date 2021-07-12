# x=0
# x = x + 1
# print(x)


# y=10
# y = y-1
# print(y)


# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
    
# print('Despegue!')



def factorial(n: int) -> int:
    resultado = 1
    numero_actual = 2
    while numero_actual <= n:
        resultado = resultado * numero_actual
        numero_actual += 1
    return resultado