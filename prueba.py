class Vehiculo():
    def __init__(self, marca="", modelo="", anio=0,kilometraje=0):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio # Usar setter para validación
        self.__kilometraje = kilometraje # Usar setter para validación

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, valor):
        if valor < 1886:
            raise ValueError("El año no puede ser anterior a 1886")
        self.__anio = valor

    @property
    def kilometraje(self):
        return self.__kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if valor < 0:
            raise ValueError("El kilometraje no puede ser negativo")
        self.__kilometraje = valor

    def mostrar(self):
        return "\nMarca:\n" + "Modelo: " + self.__modelo + "Año: "+ str(self.__anio) + "Kilometraje: " + str(self.__kilometraje)

    def conducir(self, km):
        if km <= 0:
            raise ValueError("El kilometraje no puede ser negativo")
        self.__kilometraje += km
        print(self.__kilometraje)

# Crea una instancia de la clase Vehículo
mi_vehiculo = Vehiculo("Toyota","Corolla","2020")
# Muestra la información del vehículo
print(mi_vehiculo.mostrar())
# Intenta conducir 100 km
print(mi_vehiculo.conducir(100))
# Intenta actualizar el año a uno inválido
try:
    mi_vehiculo.anio = 1800 # Debe lanzar una excepción
except ValueError as e:
    print(e)
#Intenta conducir una cantidad negativa de kilómetros
try:
    mi_vehiculo.conducir(-50) # Debe lanzar una excepción
except ValueError as e:
    print(e)

######################################################################

class InventarioVehiculos:
    def __init__(self):
        self.__vehiculos = []  # Inicia como una lista vacía

    def agregar(self, *vehiculos):
        for vehiculo in vehiculos:
            self.__vehiculos.append(vehiculo)  # Agrega cada vehículo a la lista

    def mostrar_inventario(self):
        inventario = ""
        for vehiculo in self.__vehiculos:
            inventario += f"\nMarca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}, Kilometraje: {vehiculo.kilometraje}\n"
        return inventario

    def buscar_por_marca(self, marca):
        vehiculos_encontrados = [vehiculo for vehiculo in self.__vehiculos if vehiculo.marca == marca]
        if not vehiculos_encontrados:
            raise VehiculoNoEncontradoError(f"No se encontraron vehículos de la marca {marca}")
        return vehiculos_encontrados  # Devuelve una lista con los vehículos encontrados


class VehiculoNoEncontradoError(Exception):
    pass

# Creamos varios vehículos
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Ford", "Focus", 2018)
vehiculo3 = Vehiculo("Toyota", "Yaris", 2019)

# Creamos el inventario de vehículos
inventario = InventarioVehiculos()

# Agregamos los vehículos al inventario usando *args
inventario.agregar(vehiculo1, vehiculo2, vehiculo3)

# Mostramos el inventario completo
print(inventario.mostrar_inventario())

# Buscamos vehículos por marca
try:
    vehiculos_toyota = inventario.buscar_por_marca("Toyota")
    for v in vehiculos_toyota:
        print(v.mostrar())
except VehiculoNoEncontradoError as e:
    print(e)

#######################################################################

class Alumno():
    def __init__(self, nombre="", edad=0, matricula=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula

    def __str__(self):
        return f"Alumno {self.__nombre}, Edad: {self.__edad}, Matrícula: {self.__matricula}"

    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def matricula(self):
        return self.__matricula

    @edad.setter
    def edad(self, edad):
        if edad < 16:
            raise ValueError("El alumno debe ser mayor a 16")
        self.__edad = edad

    # @matricula.setter
    # def matricula(self, matricula):
    #     if matricula == [for matricula in matricula]

class AlumnoNoEncontradoError(Exception):
    pass
class MatriculaDuplicadaError(Exception):
    pass

class Grupo:
    def __init__(self):
        self.__alumnos=[]

    def agregar_alumnos(self, *alumnos):
        for alumno in alumnos:
            if any(alumno.matricula == a.matricula for a in self.__alumnos):
                raise MatriculaDuplicadaError(f"Ya existe un alumno con la matricula {alumno.matricula}")
            self.__alumnos.append(alumno)

    def mostrar_alumnos(self):
        for alumno in self.__alumnos:
            print(alumno)


    def buscar_por_matricula(self, matricula):
        for alumno in self.__alumnos:
            if alumno.matricula == matricula:
                return alumno
        raise AlumnoNoEncontradoError(f"No se encontró ningún alumno ocn la matricula {matricula}")

# Ejemplo de uso:
try:
    # Creamos varios alumnos
    alumno1 = Alumno("Ana", 20, "A001")
    alumno2 = Alumno("Luis", 19, "A002")
    alumno3 = Alumno("Maria", 22, "A003")

    # Creamos un grupo
    grupo = Grupo()

    # Agregamos los alumnos al grupo usando *args
    grupo.agregar_alumnos(alumno1, alumno2, alumno3)

    # Mostramos los alumnos en el grupo
    grupo.mostrar_alumnos()

    # Buscamos un alumno por su matrícula
    alumno_buscado = grupo.buscar_por_matricula("A001")
    print(f"Alumno encontrado: {alumno_buscado}")

    # Intentamos agregar un alumno con matrícula duplicada
    alumno4 = Alumno("Pedro", 21, "A002")  # Matrícula duplicada
    grupo.agregar_alumnos(alumno4)

except MatriculaDuplicadaError as e:
    print(e)

except AlumnoNoEncontradoError as e:
    print(e)

except ValueError as e:
    print(e)

########################################################################################

    class CuentaBancaria:
        def __init__(self, saldo_inicial=1000):
            self.saldo = saldo_inicial

        def consultar_saldo(self):
            return self.saldo

        def realizar_retiro(self, cantidad):
            try:
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser positiva")
                if cantidad > self.saldo:
                    raise SaldoInsuficienteError(self.saldo, cantidad)
                else:
                    self.saldo = self.saldo - cantidad
                    return cantidad
            except ValueError as e:
                print(e)


    class SaldoInsuficienteError(Exception):
        def __init__(self, saldo, dinero_a_retirar):
            self.saldo = saldo
            self.dinero_a_retirar = dinero_a_retirar
            # Aquí pasamos el mensaje a Exception usando super()
            super().__init__(
                f"Saldo insuficiente. Saldo actual: {self.saldo}. Cantidad que se ha intentado retirar: {self.dinero_a_retirar}")


    # Ejemplo de uso
    try:
        cuenta = CuentaBancaria(1000)
        print(f"Saldo actual: {cuenta.consultar_saldo()}")

        dinero_a_retirar = 200
        cuenta.realizar_retiro(dinero_a_retirar)
        print(f"Saldo después del retiro: {cuenta.consultar_saldo()}")

        dinero_a_retirar = 900  # Esto debería lanzar la excepción
        cuenta.realizar_retiro(dinero_a_retirar)
        print(f"Saldo después del retiro: {cuenta.consultar_saldo()}")

    except SaldoInsuficienteError as e:
        print(e)

    except ValueError as e:
        print(e)
