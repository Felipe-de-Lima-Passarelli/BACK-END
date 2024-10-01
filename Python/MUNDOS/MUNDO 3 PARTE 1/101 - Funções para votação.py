from datetime import date
def voto(ano):
    if ano < 16:
        print(f"Com {idade} anos: Voto Negado")
    elif ano <= 17 or ano > 64:
        print(f"Com {idade} anos: Voto Opcional")
    elif ano > 17:
        print(f"Com {idade} anos: Voto Obrigatório")

anoatual = date.today().year
nascimento = int(input("Digite seu ano de nascimento: "))
idade = (anoatual - nascimento)
voto(idade)
