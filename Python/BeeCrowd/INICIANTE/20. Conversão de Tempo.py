N = int(input()) #Tempo em segundos

horas = 0
minutos = 0
segundos = 0

while N >= 3600:
    horas += 1
    N = N - 3600

while N >= 60:
    minutos += 1
    N = N - 60

while N >= 1:
    segundos += 1
    N = N -1

print(f"{horas}:{minutos}:{segundos}")
