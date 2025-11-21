N = int(input())
while N < 1 or N > 100:
    N = int(input())

contagemsaque = 0
contagembloqueio = 0
contagemataque = 0
saqueponto = 0
bloqueioponto = 0
ataqueponto = 0

for i in range(0, N):
    nome = str(input())
    S, B, A = map(int, input().split())
    S1, B1, A1 = map(int,input().split())
    saqueponto += S1
    bloqueioponto += B1
    ataqueponto += A1
    contagemsaque += S
    contagembloqueio += B
    contagemataque += A

print(f"Pontos de Saque: {(saqueponto/contagemsaque) * 100:.2f} %.")
print(f"Pontos de Bloqueio: {(bloqueioponto/contagembloqueio) * 100:.2f} %.")
print(f"Pontos de Ataque: {(ataqueponto/contagemataque) * 100:.2f} %.")
