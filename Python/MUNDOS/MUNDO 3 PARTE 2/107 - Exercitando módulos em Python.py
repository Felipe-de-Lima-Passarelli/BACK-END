from Módulos import moeda107

p = float(input("Digite o preço:  R$"))
print(f"A metade de R${p} é R${moeda107.metade(p):.2f}")
print(f"O dobro de R${p} é R${moeda107.dobro(p):.2f}")
print(f"Aumentando 10%, temos R${moeda107.aumentar(p, 10):.2f}")
print(f"Reduzindo 13%, temos R${moeda107.diminuir(p, 13):.2f}")
