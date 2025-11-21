N = int(input())
C = 0
E = 0
temguardachuvacasa = 0
temguardachuvatrabalho = 0

for i in range(0, N):
    SD, SN = map(str, input().split())

    if SD == "chuva":
        if temguardachuvacasa > 0:
            temguardachuvacasa -= 1
        else:
            C += 1
        temguardachuvatrabalho += 1

    if SN == "chuva":
        if temguardachuvatrabalho > 0:
            temguardachuvatrabalho -= 1
        else:
            E += 1
        temguardachuvacasa += 1

print(C, E)
