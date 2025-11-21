testes = int(input())

for i in range(0, testes):
    H, M, O = map(int,input().split())

    if O == 1:
        print(f"{H:02}:{M:02} - A porta abriu!")
    else:
        print(f"{H:02}:{M:02} - A porta fechou!")
