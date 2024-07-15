# crear una lista de alumnos con los siguientes campos
#nombre,apellido,edad,celular,email
#1.actualizar los registros con un campo mas todos tendran el campo de programa de estudios en enfermeria
# 2. buscar el segundo registro y actualizar su edad a 50 años.
# Definición inicial de la lista de alumnos

# Definición inicial de la lista de alumnos
alumnos = [
    {"nombre": "Juan", "apellido": "Perez", "edad": 25, "celular": "123456789", "email": "juan@example.com"},
    {"nombre": "Maria", "apellido": "Gonzalez", "edad": 30, "celular": "987654321", "email": "maria@example.com"},
    {"nombre": "Carlos", "apellido": "Lopez", "edad": 28, "celular": "567890123", "email": "carlos@example.com"}
]

# Función para agregar el campo "programa_de_estudios" en "Enfermería"
def agregar_programa_de_estudios(alumno):
    alumno["programa_de_estudios"] = "Enfermería"
    return alumno

# Función para actualizar la edad del segundo registro a 50 años
def actualizar_edad(alumno):
    if alumno["nombre"] == "Maria":  # Suponiendo que "Maria" es el segundo registro
        alumno["edad"] = 50
    return alumno

# Usando map para aplicar las funciones a cada alumno
alumnos_actualizados = list(map(agregar_programa_de_estudios, alumnos))
alumnos_actualizados = list(map(actualizar_edad, alumnos_actualizados))

# Filtrar para mostrar solo los datos actualizados
alumnos_filtrados = list(filter(lambda x: x["nombre"] == "Maria", alumnos_actualizados))

# Mostrar la lista de alumnos actualizada
print("Lista de alumnos actualizada:")
for idx, alumno in enumerate(alumnos_filtrados, start=1):
    print(f"Alumno {idx}:")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Apellido: {alumno['apellido']}")
    print(f"Edad: {alumno['edad']}")
    print(f"Celular: {alumno['celular']}")
    print(f"Email: {alumno['email']}")
    print(f"Programa de estudios: {alumno['programa_de_estudios']}")
    

