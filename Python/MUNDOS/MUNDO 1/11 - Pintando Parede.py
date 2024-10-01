largura = int(input("Digite a largura da parede"))
altura = int(input("Digite a altura da parede"))
area = largura*altura
tinta = area/2

print("A área da parede é {} metros quadrado, sendo necessário {} baldes de tinta para pintar toda a parede".format(area, tinta))