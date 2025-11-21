N = int(input())
while N >= 10000:
    N = int(input())

for i in range(0, 10000):
    if i%N == 2:
        print(i)
