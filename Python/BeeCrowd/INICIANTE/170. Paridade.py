S = str(input())
contador = S.count("1")

if contador%2 == 0:
    print(S + "0")
else:
    print(S + "1")
