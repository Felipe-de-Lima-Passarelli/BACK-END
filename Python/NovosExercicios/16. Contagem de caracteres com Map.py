linguagens = ["Python", "Java", "C++", "JavaScript"]
contador = list(map(lambda name: f"Possui {len(name)} caracteres", linguagens))
print(*contador, sep = "\n")
