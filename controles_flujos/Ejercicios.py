 ejercicio 1
 # pedir al usuario que ingrese su edad
edad= int(input("por favor,ingrese su edad:"))
# verificar si la edad ingresadaes mayor o igual a 18
if edad >=18:
    print("¡eres mayor de edad!")
    else:
        print("eres menor de edad.")

        ejercicio 2

         Almacenar la contraseña en una variable
contrasena_guardada = "Contraseña123"

# Pedir al usuario que ingrese la contraseña
contrasena_usuario = input("Por favor, ingrese la contraseña: ")

# Verificar si la contraseña introducida por el usuario coincide con la guardada
if contrasena_usuario.lower() == contrasena_guardada.lower():
    print("¡La contraseña es correcta!")
else:
    print("La contraseña es incorrecta. Inténtalo de nuevo.")

    ejercicio 3

    # Pedir al usuario que ingrese un número entero positivo
numero = int(input("Por favor, ingrese un número entero positivo: "))

# Verificar si el número ingresado es positivo
if numero < 0:
    print("El número ingresado no es positivo. Inténtalo de nuevo.")
else:
    # Crear una lista con los números en la cuenta regresiva
    cuenta_regresiva = list(range(numero, -1, -1))
    
    # Imprimir la cuenta regresiva separada por comas
    cuenta_regresiva_str = ", ".join(map(str, cuenta_regresiva))
    print(cuenta_regresiva_str)cc
        




