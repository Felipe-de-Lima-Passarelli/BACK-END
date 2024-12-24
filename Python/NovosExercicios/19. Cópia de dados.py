from time import sleep

with open("Frutas.txt", "r", encoding = "utf-8") as arquivo:
    lista_de_frutas = arquivo.readlines()

with open("Copia_dados.txt", "w", encoding = "utf-8") as arquivo_novo:
    arquivo_novo.writelines(lista_de_frutas)

with open("Copia_dados.txt", "r", encoding = "utf-8") as arquivo_novo_ler:
    conteudo = arquivo_novo_ler.read()
    for linha in conteudo.splitlines():
        print(linha)
        sleep(1)

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
