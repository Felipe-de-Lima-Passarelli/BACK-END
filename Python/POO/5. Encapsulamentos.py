class Pets:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def imprimirpet(self):
        print(f"Nome do pet: {self.nome} / Peso do Pet: {self.peso}")

    def alimentarpet(self, kg):
        self.peso += kg

class Abrigo:
    __abrigo = [] #PRIVADO -> __ / PROTEGIDO -> _ / PÚBLICO ->

    def adicionarpet(self, pet):
        self.__abrigo.append(pet)

    def imprimirabrigo(self):
        for pet in self.__abrigo:
            pet.imprimirpet()

abrigo1 = Abrigo()

pet = Pets("Chucky", 35)
pet.alimentarpet(10)
abrigo1.adicionarpet(pet)

pet = Pets("Pitty", 25)
abrigo1.adicionarpet(pet)

pet = Pets("Thor", 85)
abrigo1.adicionarpet(pet)

abrigo1.imprimirabrigo()
