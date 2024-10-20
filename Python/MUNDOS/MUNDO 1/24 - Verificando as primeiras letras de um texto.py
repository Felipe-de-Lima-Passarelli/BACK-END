x = str(input("Digite o nome da sua cidade"))
Teste = x.find("Santo")

if Teste == -1:
    print("Sua cidade, chamada de {}, não começa com a palavra Santo".format(x))
else:
    print("Sua cidade, chamada de {}, começa com a palavra Santo".format(x))
