#  ##crear una lista de 5 alumnos cada alumno almacenbaremos su nombre, apellido y edad
# # incertar al final de la lista los datos  antoni
# ## eliminar de la lista si existe los datos de abel
# #buscar y mostrar el alumnos en la posocion 4 de la lista 
# # Crear la lista de alumnos

# alumnos = [
#     {"nombre": "abel", "apellido": "García", "edad": 20},
#     {"nombre": "antoni", "apellido": "López", "edad": 22},
#     {"nombre": " ruth", "apellido": "Martínez", "edad": 18},
#     {"nombre": "flor", "apellido": "Pérez", "edad": 18},
#     {"nombre": "rocio", "apellido": "Sánchez", "edad": 23}
# ]

# # Insertar los datos de "Antoni" al final de la lista
# alumnos.append({"nombre": "Antoni", "apellido": "González", "edad": 24})                    

# # Eliminar los datos de "Abel" si existen en la lista
# for alumno in alumnos:
#     if alumno["nombre"] == "Abel":
#         alumnos.remove(alumno)

# # Buscar y mostrar el alumno en la posición 4 de la lista
# if len(alumnos) > 4:
#     alumno_posicion_4 = alumnos[4]
#     print("Alumno en la posición 4:", alumno_posicion_4)
# else:
#     print("No hay suficientes alumnos en la lista para mostrar al alumno en la posición 4.")

# #crear una lista con 3 diccionarios donde tendran los datos de sus mascotas(nombre,edad,sexo,raza)
# #tareas
# #mostrar la lista con los 4 diccionarios
# # editar 3 registro y cambiarle la edad sin modificar la lista original
# #mostrar la lista original y luego la lista con el 3er registro modificado




# # Crear la lista de diccionarios
# mascotas = [
#     {"nombre": "Luna", "edad": 3, "sexo": "embra", "raza": "Labrador Retriever"},
#     {"nombre": "Max", "edad": 5, "sexo": "macho", "raza": "Golden Retriever"},
#     {"nombre": "Bella", "edad": 2,"sexo":"hembra", "raza": "Border Collie"}
# ]

# # Mostrar la lista original
# print("Lista original:")
# print(mascotas)

# # Editar 3 registros y cambiarles la edad sin modificar la lista original
# mascotas_editadas = mascotas.copy()  # Copiar la lista original para editarla sin modificar la original
# mascotas_editadas[0]["edad"] = 4  # Cambiar la edad de Luna
# mascotas_editadas[1]["edad"] = 6  # Cambiar la edad de Max
# mascotas_editadas[2]["edad"] = 3  # Cambiar la edad de Bella

# # Mostrar la lista original y la lista editada
# print("Lista original:")
# print(mascotas)
# print("Lista con el 3er registro modificado:")
# print(mascotas_editadas)

# #yo como dueño de mi mascota
# # deceo ver una lista de mis mascotas
# # para tener un resumen o control de ellos

# #yo como dueño de mi mascota
# #deceo actualisar la edad de mi mascota
# # para tener una lista correcto de mi mascota     

# # un empresario d alquiler de autos decea  guardar en una base de datos la informacion de sus vehiculos, 
# #proceso que decea automotizar con un sistemma informatico, las acciones que pueden realizar el empresario
# # son ver las listas de auto que tiene, podra tambien actualizar la lista y agregar un nuevo veiculo
# ######
# # casos de uso
# # programacion


# #Clase para representar un vehículo
# class Vehiculo:
#     pass

# # Base de datos de vehículos
# base_de_datos_vehiculos = []

# # Crear algunos vehículos de ejemplo
# vehiculo1 = Vehiculo()
# vehiculo1.marca = "Toyota"
# vehiculo1.modelo = "Corolla"
# vehiculo1.año = 2020

# vehiculo2 = Vehiculo()
# vehiculo2.marca = "Honda"
# vehiculo2.modelo = "Civic"
# vehiculo2.año = 2022
# 3.

# # Agregar los vehículos a la base de datos
# base_de_datos_vehiculos.append(vehiculo1)
# base_de_datos_vehiculos.append(vehiculo2)

# # Ver la lista de autos
# for vehiculo in base_de_datos_vehiculos:
#     print(f"Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.año}")

# # Actualizar la lista de autos
# vehiculo1.modelo = "Camry"
# print("Lista de autos actualizada:")

# # Ver la lista actualizada de autos
# for vehiculo in base_de_datos_vehiculos:
#     print(f"Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.año}")

# # Agregar un nuevo vehículo
# nuevo_vehiculo = Vehiculo()
# nuevo_vehiculo.marca = "Ford"
# nuevo_vehiculo.modelo = "Mustang"
# nuevo_vehiculo.año = 2023

# base_de_datos_vehiculos.append(nuevo_vehiculo)
# print("Nuevo vehículo agregado a la lista:")

# # Ver la lista actualizada con el nuevo vehículo
# for vehiculo in base_de_datos_vehiculos:
#     print(f"Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.año}")

    #crea una lista usando de los primeros 20 numeros primos hasiendo usos de comprencion
# unción para verificar si un número es primo
numeros_primos = [2] + [x for x in range(3, 73, 2) if all(x % y != 0 for y in range(3, int(x ** 0.5) + 1, 2))]
print(numeros_primos)