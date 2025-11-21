import re

N = int(input())
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
respostas = {
    "1": "MONDAY",
    "2": "MONDAY",
    "3": "TUESDAY",
    "4": "TUESDAY",
    "5": "WEDNESDAY",
    "6": "WEDNESDAY",
    "7": "THURSDAY",
    "8": "THURSDAY",
    "9": "FRIDAY",
    "0": "FRIDAY"
}

padrao_placa = re.compile(r"^[A-Z]{3}-\d{4}$")

for _ in range(N):
    placa = input().strip()

    if not padrao_placa.match(placa):
        print("FAILURE")
        continue

    ultimo_digito = placa[-1]
    print(respostas[ultimo_digito])
