inicio, final = input().split() #Horas do jogo
inicio = int(inicio)
final = int(final)

if inicio < final:
    tempo = final - inicio
    print(F"O JOGO DUROU {tempo} HORA(S)")
elif inicio == final:
    tempo = 24
    print(f"O JOGO DUROU {tempo} HORA(S)")
else:
    tempo = (24 - inicio) + final
    print(f"O JOGO DUROU {tempo} HORA(S)")
