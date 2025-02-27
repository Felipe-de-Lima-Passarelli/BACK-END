fibonacci = [0, 1]

num1 = 0
num2 = 1

num = int(input("Digite um valor para verificar"
                " se faz parte da sequência de Fibonacci"))

while True:
    fibonacci.append(num1 + num2)
    num1, num2 = num2, (num1 + num2)

    if fibonacci[-1] > num:
        if num in fibonacci:
            print("Pertence a sequência de Fibonacci")
        else:
            print("Não pertence a sequência de Fibonacci")
        break
