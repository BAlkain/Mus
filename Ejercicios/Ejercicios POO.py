################################
## Ejercicio 1:
################################

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)

    # Setters para validaciones
    def set_nombre(self,nombre):
        if nombre.strip()!="":
            self.__nombre = nombre
            print("Nombre validado")
        else:
            raise ValueError("Nombre invalido")

    def set_edad(self,edad):
        if edad>0:
            self.__edad = edad
            print("Edad validada")
        else:
            raise ValueError("Edad invalido")

    def set_dni(self,dni):
        if len(dni.strip())==9 and dni[:-1].isdigit() and dni[-1].isalpha():
            self.__dni = dni
            print("DNI validado")
        else:
            raise ValueError("El DNI debe tener 8 números seguidos de una letra.")

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_dni(self):
        return self.__dni

#Metodo para mostrar los datos de la persona
    def show(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")

    def edad_legal(self):
        return self.__edad >=18

#Creo instancia de la clase Persona
persona1 = Persona(nombre="Beñat",edad=23,dni="49575157Z")

#Muestro los datos de la persona
persona1.show()

#Llamo a función edad legal
print(persona1.edad_legal())

################################
## Ejercicio 2:
################################

class Cuenta:
    def __init__(self, propietario="", importe=0.0):
        self.set_propietario(propietario)
        self.importe = float(importe)

    def get_propietario(self):
        return self.propietario

    def get_importe(self):
        return self.importe

    def set_propietario(self,propietario):
        if propietario.strip() != "":
            self.propietario = propietario
            print("Propietario valido")
        else:
            raise ValueError("Propietario invalido")

    #No se introduce un setter para el importe, solo a través de introducir()/retirar()

    def mostrar(self):
        print(f"Propietario: {self.propietario}")
        print(f"Importe: {self.importe}")

    def introducir(self, cantidad):
        if cantidad > 0:
            self.importe += cantidad
        else:
            print("No se puede introducir una cantidad negativa.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.importe -= cantidad
        else:
            print("No se puede retirar una cantidad negativa.")

cuenta1 = Cuenta("Beñat",500)
cuenta1.mostrar()
cuenta1.introducir(50)
cuenta1.mostrar()
cuenta1.retirar(200)
cuenta1.mostrar()

cuenta2 = Cuenta("Maria",1000)
cuenta2.mostrar()
cuenta2.introducir(200)
cuenta2.mostrar()
cuenta2.retirar(500)
cuenta2.mostrar()

################################
## Ejercicio 3:
################################

class CuentaJoven(Cuenta):
    def __init__(self, propietario="", importe=0.0, bonificacion=0.0, edad=0):
        super().__init__(propietario, importe)
        self.bonificacion = bonificacion
        self.edad = edad

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self):
        if 0<= bonificacion >= 100:
            self.bonificacion = bonificacion
            print("Bonificación validada")
        else:
            raise ValueError("Bonificación inválida")

    def esTitularValido(self):
        return 18<= self.edad <25

    def mostrar(self):
        super().mostrar() #Se copia el mostrat de Cuenta()
        print(f"Cuenta Joven: Bonificación: {self.bonificacion}%") #Se le añade las necesidades de CuentaJoven()

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido.")

try:
    cuenta_joven1 = CuentaJoven("Ana",500,10,20)
    cuenta_joven1.mostrar()
    cuenta_joven1.introducir(50)
    cuenta_joven1.mostrar()
    cuenta_joven1.retirar(200)
    cuenta_joven1.mostrar()
except ValueError as e:
    print(e)

cuenta_joven2 = CuentaJoven("Pedro", 300, 15, 17)
cuenta_joven2.mostrar()
cuenta_joven2.retirar(100)