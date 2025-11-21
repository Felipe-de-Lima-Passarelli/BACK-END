C = int(input())

for _ in range(0, C):
    media_final_alunos = list(map(int, input().split()))
    N = media_final_alunos[0]
    media_final_alunos.pop(0)

    media_da_turma = sum(media_final_alunos)/N
    contador = 0
    for medias in media_final_alunos:
        if medias > media_da_turma:
            contador += 1

    print(f"{(contador/N) * 100:.3f}%")
