from time import sleep

maioridade = 0
homens = 0
mulheresmenor = 0

while True:
    idade = int(input("Digite sua idade: "))
    while idade <= 0:
        print("Digite uma idade válida, por favor")
        idade = int(input("Digite sua idade: "))
    sexo = str(input('''Escolha uma opção
    [F] - Feminino
    [M] - Masculino '''))
    while sexo.strip().upper() != "F" and sexo.strip().upper() != "M":
        print("Escolha uma opção válida, por favor")
        sexo = str(input('''Escolha uma opção
        [F] - Feminino
        [M] - Masculino '''))
    if idade > 18:
        maioridade += 1
    if sexo.strip().upper() == "M":
        homens += 1
    if sexo.strip().upper() == "F" and idade < 20:
        mulheresmenor += 1
    continuar = int(input('''Deseja continuar cadastrando novas pessoas?
    [0] - Sim
    [1] - Não'''))
    while continuar != 0 and continuar != 1:
        print("Por favor, escolha uma opção válida")
        continuar = int(input('''Deseja continuar cadastrando novas pessoas?
        [0] - Sim
        [1] - Não'''))
    if continuar == 0:
        print("Ok, vamos cadastrar novas pessoas, aguarde 2 segundos!")
        sleep(2)
    elif continuar == 1:
        break

print("-=-=-=-=-= Fim do programa -=-=-=-=-=")
print(f'''{maioridade} pessoas tem idade maior que 18 anos
{homens} homens foram cadastrados no sistema
{mulheresmenor} mulheres com idade menor que 20 anos foram cadastradas no sistema''')
