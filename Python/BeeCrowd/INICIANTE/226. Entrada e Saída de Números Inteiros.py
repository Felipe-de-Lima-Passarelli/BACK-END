A = int(input())
B = int(input())
C = int(input())

while A < -10000 or A > 10000 or B < 0 or B > 99 or C < 0 or C > 999:
    A = int(input())
    B = int(input())
    C = int(input())

print(f"A = {A}, B = {B}, C = {C}")
print(f"A = {A:>10}, B = {B:>10}, C = {C:>10}")
print(f"A = {A:=010}, B = {B:=010}, C = {C:=010}")
print(f"A = {A:<10}, B = {B:<10}, C = {C:<10}")
