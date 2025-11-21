N = int(input())
somatorio = 0

for _ in range(0, N):
    C, P = map(int, input().split())
    somatorio += (C/P)

if somatorio > 1:
    print("FAIL")
else:
    print("OK")
