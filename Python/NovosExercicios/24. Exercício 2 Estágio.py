frase = str(input("Digite uma frase: "))
frase = frase.upper()

if frase.count("A") != 0:
    print(f"Existe a letra [A] na frase -> [{frase}]")
    print(f"A letra [A] apareceu {frase.count("A")} vezes")
else:
    print(f"Não existe a letra [A] na frase -> [{frase}]")
