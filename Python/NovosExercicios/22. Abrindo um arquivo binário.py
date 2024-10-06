with open("Palmeiras.png", "rb") as arquivo:
    conteudo = arquivo.read()
    print(f"A imagem possui {len(conteudo)} bytes")
