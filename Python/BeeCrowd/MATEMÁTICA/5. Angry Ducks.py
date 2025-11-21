import math

g = 9.80665
pi = 3.14159

while True:
    try:
        h = float(input())
        p1, p2 = map(int, input().split())
        n = int(input())

        for _ in range(n):
            alpha, V = map(float, input().split())

            alpha_rad = alpha * pi / 180

            a = -0.5 * g
            b = V * math.sin(alpha_rad)
            c = h

            discriminante = b ** 2 - 4 * a * c
            if discriminante < 0:
                continue

            t1 = (-b + math.sqrt(discriminante)) / (2 * a)
            t2 = (-b - math.sqrt(discriminante)) / (2 * a)

            t = max(t1, t2)

            x = V * math.cos(alpha_rad) * t

            if p1 <= x <= p2:
                print(f"{x:.5f} -> DUCK")
            else:
                print(f"{x:.5f} -> NUCK")

    except EOFError:
        break
