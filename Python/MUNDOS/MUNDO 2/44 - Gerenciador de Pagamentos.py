preco = float(input("Digite o valor do produto em reais: "))
pagamento = str(input("Pagamento será à vista? Digite sim ou não"))

if pagamento.strip() == "sim":
    formaPagamento = input("O pagamento será por dinheiro, cheque ou cartão?")
    if formaPagamento.strip() == "dinheiro" or formaPagamento == "cheque":
        preco = (preco*0.9)
    else:
        preco = (preco*0.95)
else:
    parcelas = int(input("Quer parcelar em quantas vezes? Digite o número de parcelas: "))
    if parcelas <= 2:
        preco = preco
    else:
        preco = (preco*1.20)

print("Você terá que pagar R${:.2f} reais pelo produto".format(preco))
