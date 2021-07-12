# lista = [[1,3,5,7,9],[2,4,6,8,10]]
# for k in range(len(lista)):
#     suma=0
#     for x in range(len(lista[k])):
#         suma=suma+lista[k][x]
#     print(suma)



# padres=[["juan","ana"], ["carlos","maria"], ["pedro","laura"]]
# hijos=[["marcos","alberto","silvia"], [], ["oscar"]]

padres=[]
hijos=[]
for k in range(3):
    pa=input("Ingrese el nombre del padre:")
    ma=input("Ingrese el nombre de la madre:")
    padres.append([pa, ma])
    cant=int(input("Cuantos hijos tiene esta familia:"))
    hijos.append([])
    for x in range(cant):
        nom=input("Ingrese el nombre del hijo:")
        hijos[k].append(nom)

print("Listado del padre, madre y sus hijos")
for k in range(3):
    print("Padre:",padres[k][0])
    print("Madre:",padres[k][1])
    for x in range(len(hijos[k])):
        print("Hijos:",hijos[k][x])

print("Listado del padre, madre y sus hijos")
for x in range(3):
    print("padre:",padres[x][0])
    print("cantidad de hijos:",len(hijos[x]))


