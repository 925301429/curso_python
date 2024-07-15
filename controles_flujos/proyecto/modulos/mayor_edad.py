def mayor_edad(edad):
    """funciones para saver si una persona es mayor de edad"""
    if edad >=18:
        print("es mayor de edad")
    else:
        print("en mayor de edad")

def es_mayor(lista):      
    """funciones para saber el numero mayor de una lista"""       
    mayor=lista[0]
    for n in lista:
        if n > mayor:
            mayor=n
    return mayor