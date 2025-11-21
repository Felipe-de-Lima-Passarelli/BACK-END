C = int(input())

biblioteca = {
    0: "PROXYCITY",
    1: "P.Y.N.G.",
    2: "DNSUEY!",
    3: "SERVERS",
    4: "HOST!",
    5: "CRIPTONIZE",
    6: "OFFLINE DAY",
    7: "SALT",
    8: "ANSWER!",
    9: "RAR?",
    10: "WIFI ANTENNAS"
}

for _ in range(0, C):
    X, Y = map(int, input().split())
    soma = (X + Y)
    print(biblioteca[soma])
