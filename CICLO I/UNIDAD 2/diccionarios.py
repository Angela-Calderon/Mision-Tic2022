# persona = {'nombre': 'Pedro', 'apellido': 'Perez', 'edad': 28}
# print(persona)

# print(persona['apellido'])


# persona['edad'] = 29
# print(persona)


# diccionarioEjemploExcel ={"nombre":5+2,"telefono":3363692, "edad":33, "ciudad":"Pereira"}
# print(diccionarioEjemploExcel)


# diccionario = dict(total= 55, descuento= True, subtotal= 15)
# print(diccionario)


# diccionario = {"total": 55, 10: "Curso de Python", 2.0: True}
# print(diccionario)


# usuario = {
#     'nombre': 'Nombre del usuario',
#     'edad' : 23, 
#     'curso': 'Curso de Python',
#     'skills':{
#         'programacion' : True,
#         'base_de_datos': False
#     },
#     'No medallas' : 10
# }

# # print(usuario)
# print(usuario['curso'])
# print(usuario['skills'])
# print(usuario['skills']['base_de_datos'])


# diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
# print(diccionario)
# print(diccionario.keys())
# print(diccionario.values())



# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# versiones.clear()
# print(versiones)


# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# otra_versiones = versiones.copy()
# print(versiones == otra_versiones)
# print(versiones)
# print(otra_versiones)


# secuencia = ('python', 'zope', 'plone')
# versiones = dict.fromkeys(secuencia)
# print("Nuevo Diccionario : %s" %  str(versiones))
# print("Nuevo Diccionario : {}".format(str(versiones)))


# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones.get('plone'))
# print(versiones.get('php'))


# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones.items())


# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# print(versiones.pop('zope'))
# print(versiones)


# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# versiones_adicional = dict(django=2.1)
# print(versiones_adicional)
# versiones.update(versiones_adicional)
# print(versiones)


# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(len(versiones))

# usuario = {
#     'nombre': 'Nombre del usuario',
#     'edad' : 23, 
#     'curso': 'Curso de Python',
#     'skills':{
#         'programacion' : True,
#         'base_de_datos': False
#     },
#     'No medallas' : 10
# }

# print(len(usuario))



# versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
# print(versiones)

# del versiones["python"]
# print(versiones)


# Estudiantes = {  'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
#                  'Alumno2':{'nombre':'David', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   }

#print(Estudiantes)

# if Estudiantes['Alumno1']['nombre'] == Estudiantes['Alumno2']['nombre']:
#     print("Los nombres son iguales")
# else:
#     print('Los nombres son diferentes')



# Informacion = {  'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
#                  'Alumno2':{'nombre':'David', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   }

# if Informacion['Alumno1']['edad'] > Informacion['Alumno2']['edad']:
    
#     print(str(Informacion['Alumno1']['nombre']) + ' es mayor') 
#     mayor = {'nombremayor':Informacion['Alumno1']['nombre'], 'edadmayor':Informacion['Alumno1']['edad'] }
    
# elif Informacion['Alumno1']['edad'] < Informacion['Alumno2']['edad']:
    
#     print(str(Informacion['Alumno1']['nombre']) + ' es menor') 
    
#     mayor = {'nombremayor':Informacion['Alumno2']['nombre'], 'edadmayor':Informacion['Alumno2']['edad'] }
    
# print(mayor)




# def promedioNotas(dicNotas):
#     sumatoria = 0
#     sumatoria += dicNotas["nota1"]
#     sumatoria += dicNotas["nota2"]
#     sumatoria += dicNotas["nota3"]
#     sumatoria += dicNotas["nota4"]
#     promedio = round(sumatoria/4, 2)
#     return promedio

# dicNotas = {
#             "nota1":3.0,
#             "nota2":2.1,
#             "nota3":5.0,
#             "nota4":4.7
# }

# print("El promedio es:",promedioNotas(dicNotas))


def reportarPromedio(dicReporte):
    return dicReporte["estudiante"]+" = "+str(dicReporte["promedio"])


def generarReporteNotas(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas["nota1"]
    sumatoria += dicNotas["nota2"]
    sumatoria += dicNotas["nota3"]
    sumatoria += dicNotas["nota4"]
    promedio = round(sumatoria/4, 2)
    reporteNotas = {
                    "promedio":promedio,
                    "estudiante":dicNotas["estudiante"]
    }
    return reporteNotas

dicNotas = {
            "estudiante": "Beneficiario Rodriguez",
            "nota1":3.0,
            "nota2":2.1,
            "nota3":5.0,
            "nota4":4.7
}

print(reportarPromedio(generarReporteNotas(dicNotas)))