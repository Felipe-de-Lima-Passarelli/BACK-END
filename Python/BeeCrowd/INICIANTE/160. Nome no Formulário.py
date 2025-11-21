L = str(input())
while len(L) < 1 or len(L) > 500:
    L = str(input())

if len(L) <= 80:
    print("YES")
else:
    print("NO")
