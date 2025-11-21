primeiro = str(input())
while primeiro != "vertebrado" and primeiro != "invertebrado":
    primeiro = str(input())

segundo = str(input())
while segundo != "ave" and segundo != "mamifero" and segundo != "inseto" and segundo != "anelideo":
    segundo = str(input())

terceiro = str(input())
while terceiro != "carnivoro" and terceiro != "onivoro" and terceiro != "herbivoro" and terceiro != "hematofago":
    terceiro = str(input())

if primeiro == "vertebrado":
    if segundo == "ave":
        if terceiro == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if terceiro == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if segundo == "inseto":
        if terceiro == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if terceiro == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
