
# var1 = 10
# var2 = 30
# var3 = 120 
# var4 = 500

# maximo = max(var1, var2, var3, var4)
# print(maximo)

# minimo = min(var1, var2, var3, var4)
# print(minimo)

# var1 = 10
# var2 = 30
# var3 = 120 
# var4 = 500

# sum(var1, var2, var3, var4)
# x = range(5) #DEVUELVE LOS NUMERO DEL 0 AL 4 
# print(x)
# x = range(0,5) 
# print(list(x))

# len(x) #Esto tendria un tamaño de 4 numeros {0, 1, 2, 3, 4}


def saludar(nombre, apellido):
    saludo = "Hola " + nombre + " " + apellido
    return saludo

# mi_saludo = saludar("Juan", "Perez")
# print(mi_saludo)


# def imprime_Cosas():
#     print("La clase esta genial")   #Se debe explicar de la indentacion de python y de como se ejecutan las instrucciones
#     print('Python es lo maximo')

# imprime_Cosas()

# def repetir_funciones():
#     imprime_Cosas()
#     imprime_Cosas()
    
# repetir_funciones()

# def saludar(nombre, mensaje ="Hola"):
#     print(mensaje, nombre)

# saludar('Pepe Grillo', 'Buenos dias')


def saludar(nombre, mensaje ="Hola"):
    print(mensaje, nombre)

saludar(mensaje='Buenos dias' , nombre='Juancho')

