lista = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print(40*"-")
print(f"{"LISTAGEM DE PREÇOS":^40}")

for c in range(len(lista) - 1):
    if c == 0 or c%2 == 0:
        print(f"{lista[c]}....................R$   ", end = "")
        print(f"{lista[c + 1]:.2f} reais")

print(40*"-")
