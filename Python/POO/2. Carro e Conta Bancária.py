from time import sleep


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

    def ligar_motor(self):
        print(f"O motor do {self.marca} está ligado")

    def desligar_motor(self):
        print(f"O motor do {self.marca} está desligado")

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)

carro1.exibir_detalhes()
sleep(1)
carro2.exibir_detalhes()
sleep(1)

carro1.ligar_motor()
carro2.desligar_motor()

class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def saldoatual(self):
        print(f"Seu saldo atual é {self.saldo}")

    def depositar(self, valor = 0):
        self.saldo += valor
        print(f"Você adicionou {valor} ao seu saldo. Atualmente você tem R${self.saldo} reais")

    def sacar(self, valor = 0):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Você retirou {valor} do seu saldo. Atualmente você tem R${self.saldo} reais")

banco_1 = ContaBancaria("Felipe de Lima Passarelli", 1000)
sleep(1)
banco_1.saldoatual()
sleep(1)
banco_1.depositar(200)
sleep(1)
banco_1.sacar(1100)
sleep(1)
banco_1.saldoatual()
sleep(1)
banco_1.sacar(200)
