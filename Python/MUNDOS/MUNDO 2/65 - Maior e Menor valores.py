x = int(input("Digite um número inteiro positivo"))
soma = 0
maior = x
menor = x
escolha = 0
contagem = 0

if x <= 0:
    print("Digite um número válido")
else:
    while escolha == 0:
        soma += x
        contagem += 1
        if x > maior:
            maior = x
        if x < menor:
            menor = x
        escolha = int(input('''Escolha uma opção: 
        [0] - Desejo adicionar mais números
        [1] - Desejo finalizar o programa'''))
        if escolha == 0:
            x = int(input("Digite um número inteiro positivo"))

    print('''A média dos valores inseridos deu: {:.2f}
    O maior número inserido foi: {}
    O menor número inserido foi: {}'''.format((soma/contagem), maior, menor))
