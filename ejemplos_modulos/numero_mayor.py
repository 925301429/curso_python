def f_numero_mayor(lista:list):
    numero_mayor=lista[0]
    for n in lista:
        if n>numero_mayor:
            numero_mayor=n
    return numero_mayor