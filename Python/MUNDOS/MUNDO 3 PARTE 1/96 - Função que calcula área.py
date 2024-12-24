def area(largura, comprimento):
    areaterreno = largura * comprimento
    print(f"A área do seu terreno {largura} x {comprimento} é de {areaterreno}m²")

print("Controle de Terrenos")
print(25*"-")

a = float(input("LARGURA (m): "))
b = float(input("COMPRIMENTO (m): "))
area(a, b)
