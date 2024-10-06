nomes = ["Maria", "João", "Ana"]
saudacaoNomes = list(map(lambda name: f"Olá {name}", nomes))
print(*saudacaoNomes, sep = "\n")
