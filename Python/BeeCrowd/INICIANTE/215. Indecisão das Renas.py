numeros = list(map(int, input().split()))
x = sum(numeros)
respostas = {
    1: "Dasher",
    2: "Dancer",
    3: "Prancer",
    4: "Vixen",
    5: "Comet",
    6: "Cupid",
    7: "Donner",
    8: "Blitzen",
    0: "Rudolph"
}

print(respostas[x%9])
