velocidade = float(input("Digite a velocidade do seu carro ao passar no radar, em Km/h: "))

if velocidade > 80:
    print("Você foi multado por estar dirigindo com a velocidade de {} Km/h.".format(velocidade))
    x = (velocidade - 80)
    multa = (x*7)
    print("Sua multa tem o valor de R${:.2f} reais".format(multa))
else:
    print("Parabéns, continue dirigindo sempre com segurança!")
