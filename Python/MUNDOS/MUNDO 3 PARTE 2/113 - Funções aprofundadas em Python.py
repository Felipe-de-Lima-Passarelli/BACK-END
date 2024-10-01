from time import sleep


def leiaint(frase):
    while True:
        try:
            y = int(input(frase))
        except (ValueError, TypeError):
            print("\033[1;31mERRO: por favor, digite um número inteiro válido\033[m")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return y

def leiafloat(frase):
    while True:
        try:
            y = float(input(frase))
        except (ValueError, TypeError):
            print("\033[1;31mERRO: por favor, digite um número real válido\033[m")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return y

inteiro = leiaint("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {inteiro}")
sleep(1)
decimal = leiafloat("Digite um número real: ")
print(f"Você acabou de digitar o número {decimal}")
