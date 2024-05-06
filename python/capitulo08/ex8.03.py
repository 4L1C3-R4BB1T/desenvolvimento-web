class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print(f"Saldo: {self.saldo}")


conta = ContaBancaria()

conta.depositar(100)
conta.sacar(54)
conta.sacar(90)
conta.exibir_saldo()
