x = 0
y = 1
listax = [0, 1, 2]
listay = [1, 2, 3, 4]

while True:
    for i in range(0, 3):
        if x in listax:
            x = int(x)
        if y in listay:
            y = int(y)
        print(f"I={x} J={y}")
        y += 1
    x += 0.2
    y -= 2.8
    x = round(x, 1)
    y = round(y, 1)
    if x == 2:
        for i in range(0, 3):
            if x in listax:
                x = int(x)
            if y in listay:
                y = int(y)
            print(f"I={x} J={y}")
            y += 1
        break
