B = int(input())
G = int(input())
if G%2 != 0:
    G -= 1

if B*2 < G:
    print(f"Faltam {(G - (2*B))/2:.0f} bolinha(s)")
else:
    print("Amelia tem todas bolinhas!")
