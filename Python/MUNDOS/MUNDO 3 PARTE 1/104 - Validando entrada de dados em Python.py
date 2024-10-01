def leiaint(frase):
    while True:
        y = input(frase)
        if y.isdigit():
            return int(y)
        else:
            print("Por favor, digite um número")


x = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {x}")
