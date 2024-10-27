primeironum = 0
segundonum = 1
fibonacci = [0, 1]

x = int(input("Digite um número inteiro"))

for i in range(0, x):
    terceironum = primeironum + segundonum
    fibonacci.append(terceironum)
    primeironum, segundonum = segundonum, terceironum

if x in fibonacci:
    print(f"O número {x} pertence a sequência")
else:
    print(f"O número {x} não pertence a sequência")
