pessoas = dict()
listaNome = []
listaSexo = []
listaMulheres = []
listaIdadeAcima = []
listaIdade = []
somaIdades = 0
i = 0
c = 0
t = 0

while True:
 listaNome.append(str(input("Digite seu nome: ")))
 listaSexo.append(str(input("Digite seu sexo [M/F]: ")))
 listaIdade.append(int(input("Digite sua idade: ")))
 escolha = int(input('''Deseja cadastrar mais pessoas?
 [0] - Não
 [1] - Sim '''))
 if escolha == 0:
     break

pessoas["Nome"] = listaNome
pessoas["Sexo"] = listaSexo
pessoas["Idade"] = listaIdade

while i < len(listaIdade):
    somaIdades += listaIdade[i]
    i += 1

print(f"Foram cadastradas no total {len(list(pessoas.values())[0])} pessoas")
print(f"A média de idade do grupo é: {somaIdades/(len(list(pessoas.values())[0]))}")

while c < (len(pessoas["Sexo"])):
    if pessoas["Sexo"][c].strip() in "Ff":
        listaMulheres.append(pessoas["Nome"][c])
    c += 1

while t < (len(pessoas["Idade"])):
    if pessoas["Idade"][t] > (somaIdades/(len(list(pessoas.values())[0]))):
        listaIdadeAcima.append(pessoas["Nome"][t])
    t += 1

print(f"As mulheres são: {listaMulheres}")
print(f"A lista das pessoas com idade acima da média é: {listaIdadeAcima}")
