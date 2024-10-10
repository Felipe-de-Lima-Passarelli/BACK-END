linguagens = ["Python", "Java", "C++", "JavaScript"]
contador = list(map(lambda name: f"Possui {len(name)} caracteres", linguagens))
print(*contador, sep = "\n")

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
