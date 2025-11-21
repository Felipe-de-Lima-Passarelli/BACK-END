while True:
    try:
        N = int(input())
        votos = list(map(int, input().split()))
        while len(votos) != N:
            votos = map(int, input().split())

        if (votos.count(1)/N) < (2/3):
            print("acusacao arquivada")
        else:
            print("impeachment")
    except EOFError:
        break
