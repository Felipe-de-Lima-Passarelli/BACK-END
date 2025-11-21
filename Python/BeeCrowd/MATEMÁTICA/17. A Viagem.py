while True:
    n = int(input())
    if n == 0:
        break
    alunos_gastos = []

    for _ in range(0, n):
        alunos_gastos.append(float(input()))

    resposta_final = 0
    media = sum(alunos_gastos)/n

    for valores in alunos_gastos:
        if valores < media:
            resposta_final += valores - media

    print(f"${abs(resposta_final):.2f}")
