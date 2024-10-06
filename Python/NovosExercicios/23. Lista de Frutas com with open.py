from time import sleep

with open("Frutas.txt", "w", encoding = "utf-8") as arquivo:
    arquivo.write("1ª Fruta: Abacaxi\n")
    arquivo.write("2ª Fruta: Banana\n")
    arquivo.write("3ª Fruta: Laranja\n")
    arquivo.write("4ª Fruta: Goiaba\n")
    arquivo.write("5ª Fruta: Limão\n")

with open("Frutas.txt", "r", encoding = "utf-8") as arquivo:
    for linhas in arquivo:
        print(linhas)
        sleep(1)

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
