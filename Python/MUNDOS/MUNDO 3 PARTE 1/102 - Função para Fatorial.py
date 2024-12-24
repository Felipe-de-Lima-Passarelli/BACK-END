def fatorial(num, show = False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :print: O valor do Fatorial de um número n.
    """
    total = 1
    if not show:
        for i in range(num, 0, -1):
            total *= i
        print(total)
    else:
        for i in range(num, 0, -1):
            total *= i
            if i != 1:
                print(f"{i} x ", end = "")
            else:
                print(f"{i} = ", end = "")
        print(total)

fatorial(8, True)
help(fatorial)
