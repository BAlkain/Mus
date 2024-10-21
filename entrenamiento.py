# class CuentaBancaria:
#     def __init__(self, saldo_inicial=1000):
#         self.saldo = saldo_inicial
#
#     def consultar_saldo(self):
#         return self.saldo
#
#     def realizar_retiro(self, cantidad):
#         try:
#             if cantidad <= 0:
#                 raise ValueError("La cantidad debe ser positiva")
#             if cantidad > self.saldo:
#                 raise SaldoInsuficienteError(self.saldo, cantidad)
#             else:
#                 self.saldo = self.saldo - cantidad
#                 return cantidad
#         except ValueError as e:
#             print(e)
#
# class SaldoInsuficienteError(Exception):
#     def __init__(self, saldo, dinero_a_retirar):
#         self.saldo = saldo
#         self.dinero_a_retirar = dinero_a_retirar
#         # Aquí pasamos el mensaje a Exception usando super()
#         super().__init__(f"Saldo insuficiente. Saldo actual: {self.saldo}. Cantidad que se ha intentado retirar: {self.dinero_a_retirar}")
#
# # Ejemplo de uso
# try:
#     cuenta = CuentaBancaria(1000)
#     print(f"Saldo actual: {cuenta.consultar_saldo()}")
#
#     dinero_a_retirar = 200
#     cuenta.realizar_retiro(dinero_a_retirar)
#     print(f"Saldo después del retiro: {cuenta.consultar_saldo()}")
#
#     dinero_a_retirar = 900  # Esto debería lanzar la excepción
#     cuenta.realizar_retiro(dinero_a_retirar)
#     print(f"Saldo después del retiro: {cuenta.consultar_saldo()}")
#
# except SaldoInsuficienteError as e:
#     print(e)
#
# except ValueError as e:
#     print(e)

#########################################################################

class ExcepcionAnioInvalido(Exception):
    def __init__(self):
        print(f"El año de publicación no puede ser anterior a 1440")

class Libro:
    def __init__(self, titulo,autor,anio_publicacion,copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.copias_disponibles = copias_disponibles

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self,titulo):
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self,autor):
        self._autor = autor

    @property
    def anio_publicacion(self):
        return self._anio_publicacion

    @anio_publicacion.setter
    def anio_publicacion(self,anio_publicacion):
        if anio_publicacion <1440:
            raise ExcepcionAnioInvalido()
        else:
            self._anio_publicacion = anio_publicacion

    @property
    def copias_disponibles(self, valor):
        assert valor >= 0, "El número de copias disponibles no puede ser negativa"
        self._copias_disponibles = valor

    @copias_disponibles.setter
    def copias_disponibles(self,copias_disponibles):
        self._copias_disponibles = copias_disponibles

class LibroPrestado(Libro):
    def __init__(self,titulo,autor,anio_publicacion,copias_disponibles,prestado=True):
        super().__init__(titulo,autor,anio_publicacion,copias_disponibles)
        self.__prestado = prestado

    def prestar(self):
        if self.copias_disponibles <= 0:
            raise ValueError("No hay copias disponibles")
        self.prestados+=1
        self.copias_disponibles