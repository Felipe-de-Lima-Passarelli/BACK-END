def converter_bin(arquivo):
    with open("Frutas.txt", "r", encoding = "utf-8") as arquivo:
        conteudo = arquivo.read()

    with open("Frutas.bin", "wb") as arquivo_novo:
        arquivo_novo.write(conteudo.encode("utf-8"))
        print("Arquivo binário criado com sucesso")

converter_bin("Frutas.txt")

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
