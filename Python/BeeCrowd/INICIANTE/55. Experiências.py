N = int(input())
totalcobaias = 0
totaldecoelhos = 0
totalderatos = 0
totaldesapos = 0

for i in range(0, N):
    quantidade, animal = input().split()
    quantidade = int(quantidade)
    animal = str(animal)
    totalcobaias += quantidade
    if animal == "C":
        totaldecoelhos += quantidade
    elif animal == "R":
        totalderatos += quantidade
    else:
        totaldesapos += quantidade

totalanimais = totaldecoelhos + totalderatos + totaldesapos
porcentagemcoelhos = (totaldecoelhos/totalanimais) * 100
porcentagemratos = (totalderatos/totalanimais) * 100
porcentagemsapos = (totaldesapos/totalanimais) * 100

print(f"Total: {totalcobaias} cobaias")
print(f"Total de coelhos: {totaldecoelhos}")
print(f"Total de ratos: {totalderatos}")
print(f"Total de sapos: {totaldesapos}")
print(f"Percentual de coelhos: {porcentagemcoelhos:.2f} %")
print(f"Percentual de ratos: {porcentagemratos:.2f} %")
print(f"Percentual de sapos: {porcentagemsapos:.2f} %")
