contador = 0

with open("Linhas.txt", "w", encoding = "utf-8") as arquivo:
    arquivo.write("Esta é a 1ª Linha\n")
    arquivo.write("Esta é a 2ª Linha\n")
    arquivo.write("Esta é a 3ª Linha\n")
    arquivo.write("Esta é a 4ª Linha\n")
    arquivo.write("Esta é a 5ª Linha\n")
    arquivo.write("Esta é a 6ª Linha\n")
    arquivo.write("Esta é a 7ª Linha\n")
    arquivo.write("Esta é a 8ª Linha\n")
    arquivo.write("Esta é a 9ª Linha\n")
    arquivo.write("Esta é a 10ª Linha\n")

with open("Linhas.txt", "r", encoding = "utf-8") as arquivo:
    for linhas in arquivo:
        contador += 1
    print(f"O arquivo possui {contador} linhas no total")

with open("Linhas.txt", "r", encoding = "utf-8") as arquivo:
    linhatotal = arquivo.readlines()
    print(f"O arquivo possui {len(linhatotal)} linhas no total")

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
