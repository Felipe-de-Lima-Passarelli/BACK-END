import sys

sys.set_int_max_str_digits(sys.maxsize)

divisores = [1]
while True:
    try:
        n = int(input())
        i = 2
        for numeros in divisores:
            if numeros % n == 0:
                print(len(str(numeros)))
                break
            else:
                divisores.append(int(str("1" * i)))
                i += 1

    except EOFError:
        break
