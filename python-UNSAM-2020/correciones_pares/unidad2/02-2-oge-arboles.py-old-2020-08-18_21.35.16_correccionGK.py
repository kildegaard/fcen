import csv

def abrir_archivo():
    """Abre el archivo de arbolado y devuelve una lista de diccionarios"""
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    #obtenemos los encabezados
    with open(nombre_archivo, 'r') as f1:
        #Com: Copado el método .readlines()! Te lo robo
        encabezados = f1.readlines()[0].split(',')
    # abrimos el archivo y guardamos los datos(dicc) en una lista arboles
    with open(nombre_archivo) as f:
        filas = list(csv.reader(f))
        arboles = []
        for fila in filas:
            arboles.append(dict(zip(encabezados,fila)))
    return arboles

#Com: Muy bueno el uso del -> Tuve que googlear para ver que es una anotación! Segundo robo xD
def leer_parques(parque: str = 'AVELLANEDA, NICOLÁS, Pres.') -> list:
    """Retorna una lista de diccionarios donde coincide con el parque
        Muestra por defecto los arboles del parque Pres. Nicolás Avellaneda
       Si no encuentra nada retorna un mensaje"""
    arboles = abrir_archivo()
    mostrar = []
    for arbol in arboles:
        if arbol['espacio_ve'] == parque:
            mostrar.append(arbol)
    #Com: Me parece poco claro el return, seguramente se puede hacer de otra forma!
    return "No encontramos datos en ese parque" if not mostrar else mostrar

arboles_en_parque = leer_parques(parque="GENERAL PAZ")
# print(len(arboles_en_parque))


def especies(parque: str):
    """ Devuelve un set de los arboles en el parque
        Si no encuentra nada retorna un mensaje
    """
    arboles = leer_parques('GENERAL PAZ')
    mostrar = []
    #Com: Gracias por enseñarme esto (isinstance). Pero dado que es TU código, no hace falta que lo chequees!
    if isinstance(arboles, list):
        for arbol in arboles:
            mostrar.append(arbol['nombre_com'])
    return "No encontramos datos en ese parque" if not mostrar else set(mostrar)

print(especies('GENERAL PAZ'))

def obtener_alturas(lista_parques: list, especie: str):
    tabla = []
    for parque in lista_parques:
        arboles = leer_parques(parque)
        alturas = []
        if isinstance(arboles, list):
            for arbol in arboles:
                if arbol['nombre_com'] == especie:
                    alturas.append(float(arbol['altura_tot']))
            if alturas:
                #Com: esto está bueno para ahorrar líneas pero, en mi opinión, perdés legibilidad de código
                maximo, promedio = round(max(alturas), 2), round(sum(alturas)/len(alturas), 2)
                tabla.append({'parque': parque, 'max':maximo, 'prom':promedio})
        else:
            tabla.append(f'No encontramos el parque {parque}')
    return "No encontramos esa especie" if not tabla else tabla

# print(obtener_alturas(lista_parques=['GENERAL PAZ', 'EJERCITO DE LOS ANDES', 'CENTENARIO'], especie='Jacarandá'))
