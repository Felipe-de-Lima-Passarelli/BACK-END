x = 1
y = 60

while True:
    print(f"I={x} J={y}")
    x += 3
    y -= 5
    if y == 0:
        print(f"I={x} J={y}")
        break
