from time import sleep
valor = 0
produtosmais1000 = 0
barato = 9999
nomebarato = ""

while True:
    nome = str(input("Digite o nome do produto"))
    preco = float(input(f"Digite o valor do produto: \033[1;97m{nome}\033[m em reais"))
    valor += preco
    if preco > 1000:
        produtosmais1000 += 1
    if preco < barato:
        nomebarato = nome

    escolha = int(input('''Escolha uma opção
    [0] - Cadastrar novo produto
    [1] - Finalizar programa'''))
    while escolha != 0 and escolha != 1:
        escolha = int(input('''Por favor, escolha uma opção válida
        [0] - Cadastrar novo produto
        [1] - Finalizar programa'''))
    if escolha == 0:
        print("-=-=-=-=-= PROCESSANDO -=-=-=-=-=")
        sleep(2)
    else:
        break
print(f'''O total gasto na loja foi: {valor}
{produtosmais1000} produtos custaram mais que R$1000,00 reais
O nome do produto mais barato foi: {nomebarato}''')
