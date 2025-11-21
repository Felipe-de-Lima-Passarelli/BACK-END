x = 1
y = 7

while True:
    for i in range(0, 3):
        print(f"I={x} J={y}")
        y -= 1
    y = 7
    x += 2
    if x == 9:
        for i in range(0, 3):
            print(f"I={x} J={y}")
            y -= 1
        break
