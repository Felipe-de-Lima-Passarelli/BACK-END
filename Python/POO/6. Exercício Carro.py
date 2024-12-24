class Carro:
    def __init__(self, cor, modelo, velocidade):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro está ligado: {self.ligado}")

    def desliga(self):
        if self.ligado:
            self.ligado = False
            print(f"O carro está ligado: {self.ligado}")

    def acelera(self, km):
        if self.ligado:
            self.velocidade += km
            print(f"A nova velocidade, apos acelerar {km}km/h é {self.velocidade}km/h")
        else:
            print("O carro está desligado no momento")

    def desacelera(self, km):
        if self.ligado:
            if self.velocidade - km < 0:
                self.velocidade = 0
            else:
                self.velocidade -= km
                print(f"A nova velocidade, apos desacelerar {km}km/h é {self.velocidade}km/h")
        else:
            print("O carro está desligado no momento")

    def __str__(self):
        return f'''Ligado: {self.ligado}
Velocidade: {self.velocidade}'''

carro1 = Carro("Azul", "Ferrari", 0)
carro1.liga()
carro1.desliga()
carro1.liga()
carro1.acelera(30)
carro1.desacelera(10)
carro1.desliga()
carro1.acelera(20)
carro1.desacelera(15)

print(carro1)
