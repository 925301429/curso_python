 ##crear una lista de 5 alumnos cada alumno almacenbaremos su nombre, apellido y edad
# incertar al final de la lista los datos  antoni
## eliminar de la lista si existe los datos de abel
#buscar y mostrar el alumnos en la posocion 4 de la lista 
# Crear la lista de alumnos

alumnos = [
    {"nombre": "abel", "apellido": "García", "edad": 20},
    {"nombre": "antoni", "apellido": "López", "edad": 22},
    {"nombre": " ruth", "apellido": "Martínez", "edad": 18},
    {"nombre": "flor", "apellido": "Pérez", "edad": 18},
    {"nombre": "rocio", "apellido": "Sánchez", "edad": 23}
]

# Insertar los datos de "Antoni" al final de la lista
alumnos.append({"nombre": "Antoni", "apellido": "González", "edad": 24})                    

# Eliminar los datos de "Abel" si existen en la lista
for alumno in alumnos:
    if alumno["nombre"] == "Abel":
        alumnos.remove(alumno)

# Buscar y mostrar el alumno en la posición 4 de la lista
if len(alumnos) > 4:
    alumno_posicion_4 = alumnos[4]
    print("Alumno en la posición 4:", alumno_posicion_4)
else:
    print("No hay suficientes alumnos en la lista para mostrar al alumno en la posición 4.")

#crear una lista con 3 diccionarios donde tendran los datos de sus mascotas(nombre,edad,sexo,raza)
#tareas
#mostrar la lista con los 4 diccionarios
# editar 3 registro y cambiarle la edad sin modificar la lista original
#mostrar la lista original y luego la lista con el 3er registro modificado




# Crear la lista de diccionarios
mascotas = [
    {"nombre": "Luna", "edad": 3, "sexo": "embra", "raza": "Labrador Retriever"},
    {"nombre": "Max", "edad": 5, "sexo": "macho", "raza": "Golden Retriever"},
    {"nombre": "Bella", "edad": 2,"sexo":"hembra", "raza": "Border Collie"}
]

# Mostrar la lista original
print("Lista original:")
print(mascotas)

# Editar 3 registros y cambiarles la edad sin modificar la lista original
mascotas_editadas = mascotas.copy()  # Copiar la lista original para editarla sin modificar la original
mascotas_editadas[0]["edad"] = 4  # Cambiar la edad de Luna
mascotas_editadas[1]["edad"] = 6  # Cambiar la edad de Max
mascotas_editadas[2]["edad"] = 3  # Cambiar la edad de Bella

# Mostrar la lista original y la lista editada
print("Lista original:")
print(mascotas)
print("Lista con el 3er registro modificado:")
print(mascotas_editadas)
