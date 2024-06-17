# #return devuelve los valores que podre  haser uso
# # crear una funcion que retorne el numero 10 ,y muestre por terminal si es par
# #siempre que el valor que retorne mi funcion se utilize en mas sentencias u operaciones haser uso de return
# def diez():
#     return 10
# if diez()%2==0:
#     print("es par")
# else:
#     print("es impar")
# #print solo muestra por terminal
# # return cuando queremos que  muestra funciones  devuelva o retorne un tiupo de dato o un tipo de dato estructurado                        
# # crear una funcion que muestre el producto de dos numeros
# def producto(a,b):
#     return a*b
# print(producto(4,8))

# #crear una funcion que me retorne una lista de tres numeros
# def lista_numero():
#     return [3,2,6]

# # print usaremos cada vez que nuestra funcion retorne un mensaje

# # crear una funcion por parametro reciba un nombre y retorne m,ensahje de bienvenida con el nombre
# def mensaje(nombre):
#     print(f"hola,{nombre}, bienvenido al chongo")
#     mensaje("jose")

# #crear una funcion que reciva por parametro una lista de numeros y devuelva el numero menor, mostrar por terminal el valor 
# # retornado por la funcion
# lista=[4,3,6,78,7]
# def Min(l):
#     minimo=l[0]
#     for n in l:
#         if n < minimo:
#             minimo=n
#             return minimo
# print(Min(lista))
 # crear una funcion que reciva como parametro el nombre y la edad de una 
 # persona mi funcion devera retornar un diccion con los datos, luego mostrat por terminal el valor de retorno 

# def crear_persona(nombre, edad):
#     persona = {
#         "nombre": nombre,
#         "edad": edad
#     }
#     return persona

# nombre = input("Ingrese el nombre de la persona: ")
# edad = int(input("Ingrese la edad de la persona: "))

# datos_persona = crear_persona(nombre, edad)
# print("Datos de la persona:", datos_persona)

# crea una funcion que reciba por argumento n numero y retorne una lista con los numeros pares

# def numeros_pares(lista_numeros):
#     # Creamos una lista vacía para almacenar los números pares
#     pares = []
    
#     # Iteramos sobre cada número en la lista
#     for numero in lista_numeros:
#         # Verificamos si el número es par (su residuo al dividirlo entre 2 es 0)
#         if numero % 2 == 0:
#             # Si es par, lo agregamos a la lista de números pares
#             pares.append(numero)
    
#     # Retornamos la lista de números pares al finalizar la iteración
#     return pares

# # Ejemplo de uso:
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares_encontrados = numeros_pares(numeros)
# print("Números pares encontrados:", pares_encontrados)

#crear tres funciones para los siguientes casos
#calcular el numero menor
# calcular el numero mayor
# calcular la suma de todos los numeros
#se le pasara por argumento n numeros

def calcular_menor(*numeros):
    if not numeros:
        return None
    return min(numeros)
def calcular_mayor(*numeros):
    if not numeros:
        return None
    return max(numeros)
def calcular_suma(*numeros):
    return sum(numeros)
# Ejemplo de uso
numeros = [5, 3, 8, 1, 2]

menor = calcular_menor(*numeros)
mayor = calcular_mayor(*numeros)
suma = calcular_suma(*numeros)

print(f"El número menor es: {menor}")
print(f"El número mayor es: {mayor}")
print(f"La suma de los números es: {suma}")

#empaqueta y desempaqueta de argumentos nominales
def alumnos(**kwargs):
    print(kwargs)
    alumnos(nombre="miguel",apellido="largo",edad=30)


