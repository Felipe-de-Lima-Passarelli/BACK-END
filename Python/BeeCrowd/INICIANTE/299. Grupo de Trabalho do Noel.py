presentes = {
    "bonecos": 8,
    "arquitetos": 4,
    "musicos": 6,
    "desenhistas": 12
}

N = int(input())
contador_boneco = 0
contador_arquiteto = 0
contador_musico = 0
contador_desenhista = 0

for _ in range(0, N):
    E, G, H = input().split()
    if G == "bonecos":
        contador_boneco += int(H)
    if G == "arquitetos":
        contador_arquiteto += int(H)
    if G == "musicos":
        contador_musico += int(H)
    if G == "desenhistas":
        contador_desenhista += int(H)

print(int(contador_boneco/presentes["bonecos"]) +
      int(contador_arquiteto/presentes["arquitetos"]) +
      int(contador_musico/presentes["musicos"]) +
      int(contador_desenhista/presentes["desenhistas"]))
