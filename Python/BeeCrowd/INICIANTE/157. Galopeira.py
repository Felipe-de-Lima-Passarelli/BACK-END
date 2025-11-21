C = int(input())

for i in range(0, C):
    palavra = str(input())
    while len(palavra) < 9 or len(palavra) > 10000:
        palavra = str(input())

    tempo = len(palavra)/100
    print(f"{tempo:.2f}")
