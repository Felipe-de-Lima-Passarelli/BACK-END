N = int(input())
i = 1
for c in range(0, N):
    X, Y = input().split()

    if Y == "bin":
        print(f"Case {i}:")
        i += 1
        print(f"{int(X, 2)} dec")
        print(f"{hex(int(X, 2))[2:]} hex")
    elif Y == "dec":
        print(f"Case {i}:")
        i += 1
        print(f"{hex(int(X))[2:]} hex")
        print(f"{bin(int(X))[2:]} bin")
    else:
        print(f"Case {i}:")
        i += 1
        X = "0x" + X
        print(f"{int(X, 16)} dec")
        print(f"{bin(int(X, 16))[2:]} bin")

    print()
