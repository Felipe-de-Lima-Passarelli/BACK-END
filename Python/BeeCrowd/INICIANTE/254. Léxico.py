alfabeto = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

A = str(input())
B = str(input())

if alfabeto[A[0]] < alfabeto[B[0]]:
    print(A)
    print(B)

elif alfabeto[A[0]] > alfabeto[B[0]]:
    print(B)
    print(A)
else:
    if len(A) <= len(B):
        for i in range(1, len(A)):
            if alfabeto[A[i]] < alfabeto[B[i]]:
                print(A)
                print(B)
                break
        print(A)
        print(B)
    else:
        for i in range(1, len(B)):
            if alfabeto[B[i]] < alfabeto[A[i]]:
                print(B)
                print(A)
                break
        print(B)
        print(A)
