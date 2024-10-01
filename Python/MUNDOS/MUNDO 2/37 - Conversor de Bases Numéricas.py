x = int(input("Digite um valor inteiro: "))
escolha = str(input("Escolha entre bin, oct ou hex"))

if escolha == "bin":
    print("O número {} para binário é: {}".format(x, bin(x)))
elif escolha == "oct":
    print("O número {} para octal é: {}".format(x, oct(x)))
else:
    print("O número {} para hexadecimal é: {}".format(x, hex(x)))
