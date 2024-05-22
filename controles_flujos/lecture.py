condicion=True
while condicion:
 if eval=input("desea continuar[S/N]:")
if eval=="S":
    print("continuas en el bucle")
    continue 
else:
print("se termino el programa")
condicion=False
break 

contador=0
while contador <=5:print(contador)
contador+=1
print(f"valor final {contador}")
# nombre= jose



# crear un programa que pida la cabntidad de notas que se debe registrar luego pedira
#las notas e imprimira el promedio.

cantidad_notas = int(input("Ingrese la cantidad de notas que desea registrar: "))
suma_notas = 0
contador = 0
while contador < cantidad_notas:
    nota = float(input(f"Ingrese la nota {contador + 1}: "))
    suma_notas += nota
    contador += 1

promedio = suma_notas / cantidad_notas
print(f"El promedio de las {cantidad_notas} notas ingresadas es: {promedio}")