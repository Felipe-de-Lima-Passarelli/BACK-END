hinicial, minicial, hfinal, mfinal = input().split()
hinicial = int(hinicial)
minicial = int(minicial)
hfinal = int(hfinal)
mfinal = int(mfinal)
horas = 0
minutos = 0

if hinicial == hfinal:
    if minicial < mfinal:
        tempototalmin = (24*60) + (mfinal - minicial)
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1
    elif minicial > mfinal:
        tempototalmin = (23*60) + ((60 - minicial) + mfinal)
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1
    else:
        tempototalmin = 24*60
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1

elif hinicial < hfinal:
    if minicial < mfinal:
        tempototalmin = ((hfinal - hinicial) * 60) + (mfinal - minicial)
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1
    elif minicial > mfinal:
        tempototalmin = (((hfinal - hinicial) - 1)*60) + ((60 - minicial) + mfinal)
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1
    else:
        tempototalmin = (hfinal - hinicial) * 60
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1

else:
    if minicial < mfinal:
        tempototalmin = ((24 - hinicial) + hfinal) * 60 + (mfinal - minicial)
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1
    elif minicial > mfinal:
        tempototalmin = ((((24 - hinicial) + hfinal) - 1) * 60) + ((60 - minicial) + mfinal)
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1
    else:
        tempototalmin = ((24 - hinicial) + hfinal) * 60
        while tempototalmin >= 60:
            horas += 1
            tempototalmin -= 60
        while tempototalmin >= 1:
            minutos += 1
            tempototalmin -= 1

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
