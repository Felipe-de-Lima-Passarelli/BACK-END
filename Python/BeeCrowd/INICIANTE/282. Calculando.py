c = 1
while True:
    m = int(input())
    if m == 0:
        break

    frase = input()
    nova_frase = ""

    i = 0
    while i < len(frase):
        if frase[i].isdigit():
            num = ""
            while i < len(frase) and frase[i].isdigit():
                num += frase[i]
                i += 1
            nova_frase += str(int(num))
        else:
            nova_frase += frase[i]
            i += 1

    print(f"Teste {c}")
    print(eval(nova_frase))
    print()
    c += 1
