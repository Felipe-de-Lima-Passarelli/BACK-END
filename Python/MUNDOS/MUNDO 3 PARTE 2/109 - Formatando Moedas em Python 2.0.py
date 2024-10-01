from Módulos import moeda109

p = float(input("Digite o preço:  R$"))
print(f"A metade de {moeda109.moeda(p)} é {moeda109.metade(p, form = True)}")
print(f"O dobro de {moeda109.moeda(p)} é {moeda109.dobro(p, form = True)}")
print(f"Aumentando 10%, temos {moeda109.aumentar(p, 10, form = True)}")
print(f"Reduzindo 13%, temos {moeda109.diminuir(p, 13, form = True)}")
