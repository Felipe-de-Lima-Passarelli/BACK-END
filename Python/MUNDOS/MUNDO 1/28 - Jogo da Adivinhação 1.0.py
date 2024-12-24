from random import choice
listaNumerica = [0, 1, 2, 3, 4, 5]
x = choice(listaNumerica)
suaEscolha = int(input("Digite um valor entre 0 a 5: "))

if suaEscolha == x:
    print("Você venceu!, Parabéns")
else:
    print("Você perdeu!, Tente novamente")
