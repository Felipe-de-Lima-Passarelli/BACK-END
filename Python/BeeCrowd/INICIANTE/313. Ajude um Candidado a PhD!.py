N = int(input())

for _ in range(0, N):
    frase = input()
    if frase == "P=NP":
        print("skipped")
    else:
        print(eval(frase))
