from time import sleep

with open("Frutas.bin", "rb") as arquivo:
    conteudo = arquivo.read().decode("utf-8")

for linha in conteudo.splitlines():
    print(linha)
    sleep(1)

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
