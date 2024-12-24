nome = str(input("Digite seu nome completo"))
Teste = nome.find("Silva")

if Teste == -1:
    print("Seu nome {}, não tem a palavra Silva".format(nome))
else:
    print("Seu nome {}, tem a palavra Silva".format(nome))
