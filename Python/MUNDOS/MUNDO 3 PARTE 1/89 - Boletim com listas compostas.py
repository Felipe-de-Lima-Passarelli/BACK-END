from time import sleep

notas = []
media = []
i = 0

while True:
    nome = str(input("Digite seu nome: "))
    nota1 = float(input("Nota da 1ª prova: "))
    nota2 = float(input("Nota da 2 ª prova: "))

    notas.append([nome, [nota1, nota2]])

    escolha = int(input('''Deseja cadastrar mais alunos?
    [0] - Não
    [1] - Sim'''))

    if escolha == 0:
        break

print(40*"-=")
print("No.   Nome        MÉDIA")
print(30*"-")
for pos, i in enumerate(notas):
    print(pos, end = "     ")
    print(i[0], end = "        ")
    print(((i[1][0])+(i[1][1]))/2)
print(30*"-")
sleep(1)

while True:
    novaescolha = int(input('''Mostrar notas de qual aluno? (999 interrompe)'''))
    if novaescolha == 999:
        break
    else:
        print(f"Notas de {notas[novaescolha][0]} são {notas[novaescolha][1]}")
        sleep(1)
print("Fim do programa")
