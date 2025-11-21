dia1 = input().split()[1]
dia1 = int(dia1)
tempo1 = input().split(":")
horas1 = int(tempo1[0])
minutos1 = int(tempo1[1])
segundos1 = int(tempo1[2])

dia2 = input().split()[1]
dia2 = int(dia2)
tempo2 = input().split(":")
horas2 = int(tempo2[0])
minutos2 = int(tempo2[1])
segundos2 = int(tempo2[2])

tempodias = dia2 - dia1
temposegundos = segundos2 - segundos1
tempominutos = minutos2 - minutos1
tempohoras = horas2 - horas1

if temposegundos < 0:
    temposegundos += 60
    tempominutos -= 1

if tempominutos < 0:
    tempominutos += 60
    tempohoras -= 1

if tempohoras < 0:
    tempohoras += 24
    tempodias -= 1

print(f"{tempodias} dia(s)")
print(f"{tempohoras} hora(s)")
print(f"{tempominutos} minuto(s)")
print(f"{temposegundos} segundo(s)")
