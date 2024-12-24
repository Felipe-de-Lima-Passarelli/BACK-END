from datetime import date
nascimento = int(input("Digite o ano em que nasceu e eu direi sua modalidade na natação: "))
ano = date.today().year
idade = (ano - nascimento)

if idade < 10:
    print("Você é da modalidade MIRIM da natação")
elif idade < 15:
    print("Você é da modalidade INFANTIL da natação")
elif idade < 20:
    print("Você é da modalidade JUNIOR da natação")
elif idade == 20:
    print("Você é da modalidade SÊNIOR da natação")
else:
    print("Você é da modalidade MASTER da natação")
