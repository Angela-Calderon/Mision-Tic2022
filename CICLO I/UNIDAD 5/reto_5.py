import pandas as pd

def analizarDatos(archivo: str, porcentaje: float) -> dict:

    df = pd.read_csv('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', sep=';')

    precios = df.groupby(['PRECIO']).size()

    cant = max(precios)

    data = precios.reset_index()
    indice= data.loc[data[0]==cant].index

    valor = data["PRECIO"][indice][0]
    

    proyeccion = valor + (valor * porcentaje)

    final = {
        "Precio seleccionado": valor,
        "Veces seleccionado": cant,
        "proyección": proyeccion
    }

    return final

print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', 0.053))
print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', 0.012))

    