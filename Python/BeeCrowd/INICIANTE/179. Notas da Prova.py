N = int(input())
while N < 0 or N > 100:
    N = int(input())

if N >= 86:
    print("A")
elif N >= 61:
    print("B")
elif N >= 36:
    print("C")
elif N >= 1:
    print("D")
else:
    print("E")
