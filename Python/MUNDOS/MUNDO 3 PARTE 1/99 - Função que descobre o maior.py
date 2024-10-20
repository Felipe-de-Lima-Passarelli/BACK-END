from time import sleep


def maior(*inteiros):
    if len(inteiros) != 0:
        print(50 * "-=")
        print("Analisando os valores passados...")
        sleep(1)
        print(inteiros, end=" ")
        print(f"-> Foram informados {len(inteiros)} valores ao todo.")
        print(f"O maior valor informado foi {max(inteiros)}")
        print(50 * "-=")
    else:
        print(50 * "-=")
        print("Analisando os valores passados...")
        sleep(1)
        print(f"-> Foram informados {0} valores ao todo.")
        print(f"O maior valor informado foi {len(inteiros)}")
        print(50 * "-=")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
