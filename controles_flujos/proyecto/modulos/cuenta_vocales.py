def cuenta_vocales(text:str):
    """funcione para contar la cantidad de vocales a que aparescan en un texto"""
    text_minuscula:str=text.lower()
    cantidad_vocales=0
    for n in text_minusculas:
        if n =="a":
            cantidad_vocales+=1
            return cantidad_vocales