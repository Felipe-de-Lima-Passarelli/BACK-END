N = int(input())
while N <= 0 or N > 1000:
    N = int(input())

romano = ""

while N >= 1000:
    romano += "M"
    N -= 1000

if N > 500:
    if N >= 900:
        romano += "CM"
        N -= 900

while N >= 500:
    romano += "D"
    N -= 500

while N >= 100:
    romano += "C"
    if romano.count("C") > 3:
        romano = romano[:-3]
        romano += "D"
    N -= 100

if N >= 90:
    romano += "XC"
    N -= 90

while N >= 50:
    romano += "L"
    N -= 50

while N >= 10:
    romano += "X"
    if romano.count("X") > 3:
        romano = romano[:-3]
        romano += "L"
    N -= 10

if N >= 9:
    romano += "IX"
    N -= 9

while N >= 5:
    romano += "V"
    N -= 5

while N >= 1:
    romano += "I"
    if romano.count("I") > 3:
        romano = romano[:-3]
        romano += "V"
    N -= 1

print(romano)
