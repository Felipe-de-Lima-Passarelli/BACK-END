from random import choice
listaNumerica = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = choice(listaNumerica)
print(x)
print("Acabei de pensar em um número entre 0 e 10, consegue acertar qual é?")
y = int(input("Digite um valor entre 0 a 10: "))
contagem = 1

while y != x:
    if y < 0 or y > 10:
        y = int(input("Número Inválido, digita um novo número entre 0 a 10: "))
    else:
        contagem += 1
        if y < x:
            y = int(input("Número incorreto, tente novamente com um número maior dessa vez: "))
        else:
            y = int(input("Número incorreto, tente novamente com um número menor dessa vez: "))

print("Você acertou, o número do computador era {}, você precisou de {} tentativas.".format(x, contagem))
