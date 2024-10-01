distancia = float(input("Digita a distância da sua viagem em Km: "))

if distancia <= 200:
    custo = (distancia * 0.50)
    print("O valor da passagem será de R${:.2f} reais".format(custo))
else:
    custo = (distancia * 0.45)
    print("O valor da passagem será de R${:.2f} reais".format(custo))
