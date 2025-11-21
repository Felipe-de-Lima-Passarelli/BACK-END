#Carro faz 12Km/L
tempo = int(input()) #Em horas
velocidade = int(input()) #Em Km/h

distancia = velocidade*tempo
gasolinagasta = distancia/12
print(f"{gasolinagasta:.3f}")
