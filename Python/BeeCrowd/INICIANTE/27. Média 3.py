#Pesos das notas -> 2, 3, 4 e 1, respectivamente.
N1, N2, N3, N4 = input().split()

N1 = round(float(N1), 1)
N2 = round(float(N2), 1)
N3 = round(float(N3), 1)
N4 = round(float(N4), 1)

media = ((N1*2) + (N2*3) + (N3*4) + (N4*1))/10
if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media >= 5:
    status = "Aluno em exame."
    notaexame = round(float(input()), 1)
    novamedia = (media + notaexame)/2
    if novamedia >= 5:
        print(f"Media: {media:.1f}")
        print("Aluno em exame.")
        print(f"Nota do exame: {notaexame}")
        print("Aluno aprovado.")
        print(f"Media final: {novamedia:.1f}")
else:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
