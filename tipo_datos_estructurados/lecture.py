texto="hola"
lista_texto=list(texto)
lista2=[e for e in texto]
texto_largo="hola como estan bienvenidos al salon"
nuevo_texto=texto_largo[16:]
nueva_lista=nuevo_texto.split(" ")
print(nueva_lista)

# dato  primitivo
lista_original=[1,2,3,4]
copia_lista=lista_original
lista_original[-1]=15
print(copia_lista)

#crear un programa que reciva una lista desordenada  y muestre por terminal una lista ordenada y la  lista previ a ser desordenada.
lista=[4,76,1,3,6,8,2]
copia_lista=lista
copia_lista.sort()
print(lista)