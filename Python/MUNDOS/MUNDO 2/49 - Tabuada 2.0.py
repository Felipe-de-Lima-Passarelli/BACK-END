x = int(input("Digite o número que queira saber a tabuada"))
for c in range(1,11):
    total = (x*c)
    print("{} x {} = {}".format(x, c, total))
