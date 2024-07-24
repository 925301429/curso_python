
def numero_menor(lista:list):
    numero_menor=lista[0]
    for n in lista:
        if n<numero_menor:
            numero_menor=n
    return numero_menor

def f_numero_mayor(lista:list):
    numero_mayor=lista[0]
    for n in lista:
        if n>numero_mayor:
            numero_mayor=n
    return numero_mayor
def f_cuenta_letras(txt:str):
    contador=0
    for n in txt:
        if n !=" ":
            contador+=1
    return contador