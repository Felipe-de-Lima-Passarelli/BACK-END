N = int(input())

for _ in range(0, N):
    h, d, g = map(int, input().split())
    if h < 200 or h > 300 or d < 50 or g < 150:
        print("Nao")
    else:
        print("Sim")
