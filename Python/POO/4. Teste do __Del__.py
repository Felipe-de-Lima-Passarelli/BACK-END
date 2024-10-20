class Pessoas:
    def __init__(self, nome):
        self.nome = nome
        print(f"O {self.nome} foi criado")

    def __del__(self):
        print(f"{self.nome} foi deletado")

eu = Pessoas("Felipe")
print(eu.nome)
