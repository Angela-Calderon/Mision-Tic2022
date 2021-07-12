def comprarEntrada(inft: str, famili: str, al_impt: str, cantidad_personas: int) -> dict:
    
    infantil = {
        "Trencito": 5000,
        "Mini rueda": 5500
    }
    
    familiar = {
        "Carrusel": 6000,
        "Carros chocones": 8000
    }
    
    alto_impacto = {
        "Barco pirata": 8500,
        "Montaña rusa": 9000
    }
    
    obsequio = ''

    if inft == "Trencito" and cantidad_personas > 2:
        obsequio = "Peluche"

    
    if famili == "Carrusel" and cantidad_personas > 3 or al_impt == "Barco pirata" and cantidad_personas > 2:
        obsequio = "Carros chocones"


    if inft != '':
        a_infantil = infantil.get(inft)
    else: a_infantil = 0

    if famili != '':
        b_familiar = familiar.get(famili)
    else: b_familiar = 0

    if al_impt != '':
        c_alto_impacto = alto_impacto.get(al_impt)
    else: c_alto_impacto = 0


    total = (a_infantil + b_familiar + c_alto_impacto)*cantidad_personas

    final = {
        "infantil" : inft,
        "familiar": famili,
        "alto impacto" : al_impt,
        "obsequio" : obsequio,
        "personas" : cantidad_personas,
        "total": total
    }

    return final


print(comprarEntrada('', 'Carros chocones', 'Barco pirata', 4))
print(comprarEntrada('Mini rueda', 'Carrusel', 'Montaña rusa', 2))