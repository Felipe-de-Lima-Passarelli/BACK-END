num = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razão da P.A: "))
i = 1

while i <= 10:
    print("{}º Termo: {}, ".format(i, num))
    num = (num + razao)
    i += 1
print("Fim da P.A")
