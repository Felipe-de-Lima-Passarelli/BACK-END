import math
CatetoOposto = float(input("Digite o comprimento do Cateto Oposto em centímetros"))
CatetoAdjacente = float(input("Digite o comprimento do Cateto Adjacente em centímetros"))
Hipotenusa = math.hypot(CatetoOposto, CatetoAdjacente)
print("A hipotenusa do triângulo inserido é: {} centímetros".format(Hipotenusa))
