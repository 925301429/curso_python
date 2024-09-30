# crear una clase bancos
#sus atributos seran nombre, apellidos,dni,numero de cuentay saldo inicial
#como metodos podremos hacer depositos retirar dinero y ver estado de cuenta.
 
class Bancos:
    def _init_(self, nombre, apellidos, DNI, numero_de_cuenta, saldo_inicial):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.numero_de_cuenta = numero_de_cuenta
        self.saldo_inicial = saldo_inicial

    def depositar(self, cantidad):
        self.saldo_inicial += cantidad
        print(f"Depósito realizado. Nuevo saldo: {self.saldo_inicial}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo_inicial:
            self.saldo_inicial -= cantidad
            print(f"Retiro realizado. Nuevo saldo: {self.saldo_inicial}")
        else:
            print("Fondos insuficientes.")

    def ver_estado_de_cuenta(self):
        print(f"Nombre: {self.nombre} {self.apellidos}")
        print(f"DNI: {self.DNI}")
        print(f"Número de cuenta: {self.numero_de_cuenta}")
        print(f"Saldo actual: {self.saldo_inicial}")
        cuenta = Bancos("Juan", "Pérez", "123456780A", "1234567890", 1000)
cuenta = Bancos("Juan", "Pérez", "12345678A", "1234567890", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.ver_estado_de_cuenta()

#ejercicio 02
#crear una clase agencia
#con sus atributos nombre y apellido del pasajero dni9 numero de aciento fecha de viaje
#sus metodos seran ingresar origen,ingresar destino,canselar viaje, ver estados
class Agencia:
    def _init_(self, nombre, apellidos, DNI, numero_de_asientos, fecha_de_viaje):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.numero_de_asientos = numero_de_asientos
        self.fecha_de_viaje = fecha_de_viaje
        self.origen = None
        self.destino = None
        self.cancelado = False

    def ingresar_origen(self, origen):
        self.origen = origen
        print(f"Origen ingresado: {self.origen}")

    def ingresar_destino(self, destino):
        self.destino = destino
        print(f"Destino ingresado: {self.destino}")

    def cancelar_viaje(self):
        self.cancelado = True
        print("Viaje cancelado.")

    def ver_estado(self):
        print(f"Nombre: {self.nombre} {self.apellidos}")
        print(f"DNI: {self.DNI}")
        print(f"Número de asientos: {self.numero_de_asientos}")
        print(f"Fecha de viaje: {self.fecha_de_viaje}")
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        print(f"Cancelado: {self.cancelado}")
        viaje = Agencia("Ana", "García", "78901234Z", 2, "2023-12-25")
        viaje.ingresar_origen("Madrid")
        viaje.ingresar_destino("Barcelona")
        viaje.ver_estado()
        viaje.cancelar_viaje()
        viaje.ver_estado()