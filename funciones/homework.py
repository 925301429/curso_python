# crear una lista de alumnos con los siguientes campos
#nombre,apellido,edad,celular,email
#1.actualizar los registros con un campo mas todos tendran el campo de programa de estudios en enfermeria
# 2. buscar el segundo registro y actualizar su edad a 50 años.
# Definición inicial de la lista de alumnos


alumnos = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 25, "celular": "987644678","email": "juan@example gmail.com"},
    {"nombre": "María", "apellido": "García", "edad": 30, "celular":"955575678","email":"maria@example gmail.com"},
    {"nombre": "Pedro", "apellido": "López", "edad": 28, "celular":"987654338","email": "pedro@example gmail.com"}
]

# 1. Agregar el campo "programa_de_estudios" a todos los registros
for alumno in alumnos:
    alumno["programa_de_estudios"] = "Enfermería"

# 2. Buscar el segundo registro y actualizar su edad a 50 años
if len(alumnos) > 1:
    alumnos[1]["edad"] = 50
else:
    print("No hay suficientes registros para actualizar la edad del segundo alumno.")

# Mostrar la lista de alumnos actualizada
for idx, alumno in enumerate(alumnos, start=1):
    print(f"Alumno {idx}:")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Apellido: {alumno['apellido']}")
    print(f"Edad: {alumno['edad']}")
    print(f"Celular: {alumno['celular']}")
    print(f"Email: {alumno['email']}")
    print(f"Programa de estudios: {alumno['programa_de_estudios']}")
    print()
