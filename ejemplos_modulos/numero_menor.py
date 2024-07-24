def numero_menor(lista:list):
    numero_menor=lista[0]
    for n in lista:
        if n<numero_menor:
            numero_menor=n
    return numero_menor