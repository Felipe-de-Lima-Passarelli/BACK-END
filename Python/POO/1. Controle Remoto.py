from time import sleep


class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

controle_1 = ControleRemoto("Preto", "10cm", "5cm", "2cm")
print(controle_1.cor)

controle_2 = ControleRemoto("Branco", "10cm", "5cm", "2cm")
print(controle_2.cor)

class Livro:
    def __init__(self, autor, nome, paginas):
        self.autor = autor
        self.nome = nome
        self.paginas = paginas

livro_1 = Livro("Felipe", "Challanger no LOL em 1 mês", 90)
print(livro_1.paginas)
