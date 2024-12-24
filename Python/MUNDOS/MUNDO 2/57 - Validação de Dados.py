sexo = str(input('''Digite seu sexo
[M] - Masculino
[F] - Feminino '''))
sexo = sexo.strip().upper()

while sexo != "M" and sexo != "F":
    sexo = str(input("Digite [M] ou [F] "))
    sexo = sexo.strip().upper()
print("FIM")
