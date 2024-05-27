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
