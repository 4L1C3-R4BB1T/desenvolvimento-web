class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError
        self.saldo -= valor


class SaldoInsuficienteError(Exception):
    def __init__(self):
        super().__init__("Saldo insuficiente")


try:
    conta = ContaBancaria()
    conta.depositar(100)
    conta.sacar(54)
    conta.sacar(90)
except SaldoInsuficienteError as e:
    print(e)
