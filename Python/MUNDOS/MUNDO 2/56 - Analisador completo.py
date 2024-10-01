somaidade = 0
idadeteste = 0
mulhercontagem = 0
nomeHomem = "Não existe nenhum homem na lista"

for i in range(0, 4):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Masculino ou Feminino?"))

    somaidade += idade

    if sexo.strip().lower() == "masculino" and idade > idadeteste:
        idadeteste = idade
        nomeHomem = nome

    if sexo.strip().lower() == "feminino" and idade < 20:
        mulhercontagem += 1

print("A idade média de todos deu: {:.0f}".format(somaidade/4))
print("O nome do homem mais velho é: {}".format(nomeHomem))
print("O número de mulheres abaixo de 20 anos é: {}".format(mulhercontagem))
