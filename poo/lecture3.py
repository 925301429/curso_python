#crear una clase de alumnos con los atributos que ustedes crea por conveniente
#luego instanciara a 4 alumnos
class alumno:
    #atributos
    def init_(self,nombre,apellido,edad,dni,genero):
           self.nombre=nombre
           self.apellido=apellido
           self.edad=edad
           self.dni=dni
           self.genero=genero
    def mostrar_alumno(self):
        return {
            "nombre":self.nombre,
            "apellido" :self.apellido,
            "edad" :self.edad,
            "dni" :self.dni,
            "genero" :self.genero,
     }
 #metodos
    def escribir(self):
         print("estoy escrivendo")
    def tarea(self,nombre_docente):
         print("haciendo la tarea de:",nombre_docente)
    def  terminar_tarea(self):
         print("terminando tarea anterior")
         
lisbet=alumno("lisbet","zevallos",18,76855002,"femenino")
print(lisbet.genero)
lisbet.tarea("alicia")
mariana=alumno("mariana","garriazo",20,75463792,"femenino")
print(mariana.genero)
