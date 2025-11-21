somaidade = 0
contador = 0

while True:
    idade = int(input())

    if idade < 0:
        break

    somaidade += idade
    contador += 1

media = somaidade/contador
print(f"{media:.2f}")
