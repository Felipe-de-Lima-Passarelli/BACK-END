cpf = str(input())
respostafinal = ""

for numeros in cpf:
    if numeros == "." or numeros == "-":
        continue
    else:
        respostafinal += numeros

for i in range(0, len(respostafinal)):
    print(respostafinal[i], end = "")
    if i == 2 or i == 5 or i == 8:
        print()
print()
