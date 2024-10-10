nomes = ["Maria", "João", "Ana"]
saudacaoNomes = list(map(lambda name: f"Olá {name}", nomes))
print(*saudacaoNomes, sep = "\n")

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
