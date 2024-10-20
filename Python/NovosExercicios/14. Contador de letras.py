with open("Texto.txt", "w", encoding = "utf-8") as arquivo:
    arquivo.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
                  "Sed sed est maximus est sollicitudin tempus id sed ligula.\n"
                  "Ut vulputate nibh vitae rutrum sollicitudin. Morbi ac mauris ante.\n"
                  "Donec semper, purus sit amet consequat commodo, neque dui dapibus nibh.\n"
                  "Vel consequat tortor nunc molestie dolor. Mauris rutrum metus eu ligula consequat pellentesque.\n")

with open("Texto.txt", "r", encoding = "utf-8") as arquivo:
    conteudo = arquivo.read()
    print(f"A parágrafo contém {len(conteudo)} letras")

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
