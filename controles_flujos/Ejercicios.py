
#  # pedir al usuario que ingrese su edad
# edad= int(input("por favor,ingrese su edad:"))
# # verificar si la edad ingresadaes mayor o igual a 18
# if edad >=18:
#     print("¡eres mayor de edad!")
# else:
#     print("eres menor de edad.")

# contrasena_guardada = "Contraseña123"

# # Pedir al usuario que ingrese la contraseña
# contrasena_usuario = input("Por favor, ingrese la contraseña: ")

# # Verificar si la contraseña introducida por el usuario coincide con la guardada
# if contrasena_usuario.lower() == contrasena_guardada.lower():
#     print("¡La contraseña es correcta!")
# else:
#     print("La contraseña es incorrecta. Inténtalo de nuevo.")

# numero = int(input("Por favor, ingrese un número entero positivo: "))

# # Verificar si el número ingresado es positivo
# if numero < 0:
#     print("El número ingresado no es positivo. Inténtalo de nuevo.")
# else:
#     # Crear una lista con los números en la cuenta regresiva
#     cuenta_regresiva = list(range(numero, -1, -1))
    
#     # Imprimir la cuenta regresiva separada por comas
#     cuenta_regresiva_str = ", ".join(map(str, cuenta_regresiva))
#     print(cuenta_regresiva_str)
    
#     # crear un programa que me cuente la cantidad de comasa y muestre
#     # sus indices
#     #OJO: tiene que pedir al ususrio

oraccion:str=input("ingrese una oracion:")
contador:int=0
for indice,letra  in enumeraste (oracion):
  if letra ==",":
   print (f"su indice es {indice}")
contador+=1
print (f"la cantidad de comas es{contador}")

# escribir  un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido
#(desde 1 hasta su edad).
edad:str=input("¿por favor ingrese su edad?")
for i in range(1,edad + 1):
   print(f"año{i}")      

# crear un programa que pida el nombre de tres personas y guarde en una variable global la ultima letra de sus nombres.
# mostrar por pantalla la bariable global con las tres ultimas letras  del nombre de cada persona
ultima_letra:str=""
for n in range(3):
  nombre:str=input("escribe tu nombre:")
#ultima_letra+=nombre[-1]
last_letter:str=nombre[-1]
ultima_letra+=last_letter
#ultima_ letra=ultima_letra+last_letter
print(ultima_letra)
#crea un programa que muestre por terminal la siguiente figura:
# a
# ee
#ooo
#uuuu

letras =["a","e","i","o","u"]
for i in range(len(letras)):
  print("#" + letras[i]*(i+1))
  

  #crea uun programa que muestra la tabla de multiplicar de 1 hasta 5

for i in range (1,6):
  print (f"la tabla de {i}")
  for j in range(1,13):
    resultado=i*j 
    print(f"{i}x{j}={resultado}")

# crea un programa que pida un numero y que se muestra la tabla de multiplicar de ese numero
numero:int=int(input("ingrese un numero:"))
print(" la tabla de multiplicar que escojistes es{numero}")
for i in range(1,13):