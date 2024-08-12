# 2. Crie um sistema para um aplicativo bancário, que possui a Classe
# ContaBancaria com as seguintes características:
# ○ Atributos: titular, saldo, numero_conta e tipo_conta.
# ○ Métodos: depositar, sacar, transferir e verificar_saldo.
# OBS: Após cada alteração no saldo, exiba o novo valor na tela.

class ContaBancaria:
    def __init__(self, titular, saldo, numero_da_conta, tipo_de_conta):
        self.titular = titular
        self.saldo = saldo
        self.numerodaConta = numero_da_conta
        self.tipodeconta = tipo_de_conta

    def depositar(self):
        valor = float(input("Digite o valor:"))
        self.saldo +=  valor
        print(f"O Novo saldo é: {self.saldo:.2f}")
        
    def sacar(self):
        valor = float(input("Digite o valor para sacar o Dindin: "))
        self.saldo -= valor
        print(f"O novo saldo é: {self.saldo:.2f}")

    def transferir(self, saldo_de_Lucas):
        valor = float(input("Digite o valor para transferir: "))
        self.saldo -= valor
        saldo_de_Lucas += valor
        return saldo_de_Lucas
    
    def verificar_saldo(self):
        print("Seu saldo é: {self.saldo}")

Lucas = ContaBancaria("melhor do mundo", 1000.90, "32-0", "CC")
Marcus = ContaBancaria("Amem", 9000.02, 33-0, "CP")
Lucas.saldo = Marcus.transferir(Lucas.saldo)
Lucas.verificar_saldo()
#Lucas.Depositar
#Marcus.sacar