from time import sleep

with open("Dados.csv", "r", encoding = "utf-8") as arquivo:
    conteudo = arquivo.read()
    for linha in conteudo.splitlines():
        print(linha)
        sleep(1)

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
