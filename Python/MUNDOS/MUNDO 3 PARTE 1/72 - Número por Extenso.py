x = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

valor = int(input("Digite um número entre 0 a 20: "))
while valor < 0 or valor > 20:
    print("Escreva um número válido, por favor")
    valor = int(input("Digite um número entre 0 a 20: "))

print(f"Você digitou o número {x[valor]}")
