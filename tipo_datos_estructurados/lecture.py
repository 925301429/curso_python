# texto="hola"
# lista_texto=list(texto)
# lista2=[e for e in texto]
# texto_largo="hola como estan bienvenidos al salon"
# nuevo_texto=texto_largo[16:]
# nueva_lista=nuevo_texto.split(" ")
# print(nueva_lista)

# # dato  primitivo
# lista_original=[1,2,3,4]
# copia_lista=lista_original
# lista_original[-1]=15
# print(copia_lista)

# #crear un programa que reciva una lista desordenada  y muestre por terminal una lista ordenada y la  lista previ a ser desordenada.
# lista=[4,76,1,3,6,8,2]
# copia_lista=lista
# copia_lista.sort()
# print(lista) 

# #crear una lista de numeros enteros del siguiente texto
# texto="1,4,8,9,6"
# nueva_lista=[]
# for n in texto.split(","):
#     nueva_lista.append(int(n))
# print(nueva_lista)
# #aplicando la tecnica valor bucle y condicion
# texto="1,4,8,9,6"
# nueva_lista=[int(n)for n in texto.split(",")if (n)%2==0]
# print(nueva_lista)

#diccionario por comprencion

lista_amigos=["abel","antohony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)
#aplicando el vlc
lista_amigos=["abel","antohony","edith","ruth"]
diccionario={amigo:len(amigo)for amigo in lista_amigos}
print(diccionario)




