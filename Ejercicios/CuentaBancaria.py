class SaldoInsuficienteError(Exception):
    """Excepción personalizada para cuando no hay saldo suficiente en la cuenta."""

    def __init__(self, saldo_actual, cantidad_retiro):
        super().__init__(f"Saldo insuficiente. Saldo actual: {saldo_actual}, Cantidad de retiro: {cantidad_retiro}")
        self.saldo_actual = saldo_actual
        self.cantidad_retiro = cantidad_retiro


class CuentaBancaria:
    def __init__(self, saldo_inicial=1000):
        """Inicializa la cuenta bancaria con un saldo predeterminado de 1000."""
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        """Devuelve el saldo actual de la cuenta."""
        return self.saldo

    def retirar_dinero(self, cantidad):
        """
        Permite retirar dinero de la cuenta.
        Si la cantidad a retirar es mayor que el saldo actual, lanza SaldoInsuficienteError.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")

        if cantidad > self.saldo:
            raise SaldoInsuficienteError(self.saldo, cantidad)

        self.saldo -= cantidad
        return self.saldo


try:
    cuenta = CuentaBancaria()  # Saldo inicial de 1000
    print(f"Saldo inicial: {cuenta.consultar_saldo()}")

    # Intentar retirar una cantidad válida
    cuenta.retirar_dinero(200)
    print(f"Saldo después del retiro: {cuenta.consultar_saldo()}")

    # Intentar retirar una cantidad mayor al saldo
    cuenta.retirar_dinero(1000)
except SaldoInsuficienteError as e:
    print(e)
except ValueError as ve:
    print(f"Error de valor: {ve}")

