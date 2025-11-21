dados = H, Z, L = list(map(int, input().split()))
dados.sort()

if dados[1] == H:
    print("huguinho")
elif dados[1] == Z:
    print("zezinho")
else:
    print("luisinho")
