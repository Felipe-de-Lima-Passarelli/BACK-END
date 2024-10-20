from datetime import date
nascimento = int(input("Digite o ano em que você nasceu: "))
ano = date.today().year
idade = (ano - nascimento)

if idade < 18:
    print("Você ainda vai se alistar ao serviço militar")
elif idade == 18:
    print("É a hora de você se alistar ao serviço militar")
else:
    print("Já passou do tempo do alistamento")
