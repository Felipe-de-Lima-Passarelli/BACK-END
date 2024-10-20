contagem50 = 0
contagem20 = 0
contagem10 = 0
contagem1 = 0

while True:
    sacado = int(input("Digite um valor positivo inteiro a ser sacado do caixa: "))

    if sacado < 0:
        print("Número inválido")
    while sacado >= 50:
        contagem50 += 1
        sacado -= 50
    while sacado >= 20:
        contagem20 += 1
        sacado -= 20
    while sacado >= 10:
        contagem10 += 1
        sacado -= 10
    while sacado >= 1:
        contagem1 += 1
        sacado -= 1

    if sacado == 0:
        break

print("-=-=-=-=-= PROCESSANDO -=-=-=-=-=")
print(f'''O valor necessário de cédulas será
Cédula de 50: {contagem50}
Cédula de 20: {contagem20}
Cédula de 10: {contagem10}
Cédula de 1: {contagem1}''')
print("-=-=-=-=-= FIM -=-=-=-=-=")
