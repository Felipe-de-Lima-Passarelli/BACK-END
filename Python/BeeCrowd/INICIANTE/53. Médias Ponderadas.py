N = int(input())

for i in range(0, N):
    nota1, nota2, nota3 = input().split()
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5))/10
    print(f"{media:.1f}")
