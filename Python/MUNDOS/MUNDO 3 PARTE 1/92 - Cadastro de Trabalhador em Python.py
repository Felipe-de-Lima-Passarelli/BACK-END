from datetime import date

dados = dict()

dados["Nome"] = str(input("Digite seu nome: "))
dados["Ano de Nascimento"] = int(input("Digite seu ano de nascimento: "))

ano = date.today().year
idade = ano - dados["Ano de Nascimento"]

dados["Carteira de Trabalho"] = str(input('''Tem carteira de trabalho? [S/N]'''))

if dados["Carteira de Trabalho"].strip() in "Ss":
    dados["Contratação"] = int(input("Ano de Contratação: "))
    dados["Salário"] = float(input("Salário: "))
    dados["Aposentadoria"] = (dados["Contratação"] + 35) - dados["Ano de Nascimento"]
    print(f"{list(dados.keys())[0]} tem o valor {dados["Nome"]}")
    print(f"Idade tem o valor {idade}")
    print(f"{list(dados.keys())[2]} tem o valor {dados["Carteira de Trabalho"]}")
    print(f"{list(dados.keys())[3]} tem o valor {dados["Contratação"]}")
    print(f"{list(dados.keys())[4]} tem o valor {dados["Salário"]}")
    print(f"{list(dados.keys())[5]} tem o valor {dados["Aposentadoria"]}")
else:
    print(f"{list(dados.keys())[0]} tem o valor {dados["Nome"]}")
    print(f"Idade tem o valor {idade}")
    print(f"{list(dados.keys())[2]} tem o valor {dados["Carteira de Trabalho"]}")
