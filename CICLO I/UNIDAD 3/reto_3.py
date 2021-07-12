def asignarCita(pacientes: list) -> str:      

    citas = 'Identificación\tPaciente\tHora\tMédico asignado\n'
    

    for paciente in pacientes:
        datos_paciente = ''
        if paciente[2] >= 8 and paciente[2] <= 12:
            paciente.append('Juan Perez') 

        elif paciente[2] >= 14 and paciente[2] < 18:
            paciente.append('Maria Lopez') 

        elif paciente[2] >= 18 and paciente[2] < 20:
            paciente.append('Pedro Rodriguez')  
        
        for dato in paciente:
            datos_paciente += f'{dato}\t'

        citas += f'\n{datos_paciente[:-1]}'
        
        
    return citas
	
print(asignarCita([['1110569478','Alexander Pinto',14], ['1110934100','Nicolas Machado',10], ['1110312456','Rebeca Vega', 8]]))