peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = (peso/(altura**2))

if imc < 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc < 25.00:
    print("Peso Ideal")
elif imc >= 25 and imc < 30.00:
    print("Sobrepeso")
elif imc >= 30 and imc < 40.00:
    print("Obesidade")
else:
    print("Obesidade Mórbida")
