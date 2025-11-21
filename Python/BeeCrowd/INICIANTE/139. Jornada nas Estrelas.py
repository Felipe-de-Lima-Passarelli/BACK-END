N = int(input())
valor = list(map(int, input().split()))
atacado = set()
total_carneiros = sum(valor)
roubo = 0
local = 0

while 0 <= local < N:
    if valor[local] > 0:
        roubo += 1
        atacado.add(local)
        if valor[local] % 2 != 0:
            valor[local] -= 1
            local += 1
        else:
            valor[local] -= 1
            local -= 1
    else:
        break

print(len(atacado), total_carneiros - roubo)
