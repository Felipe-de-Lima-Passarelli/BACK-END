x = str(input("Digite uma expressão matemática: "))
lista = []

for simbolo in x:
    if simbolo == "(":
        lista.append(simbolo)
    elif simbolo == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Expressão Válida")
else:
    print("Expressão Inválida")
