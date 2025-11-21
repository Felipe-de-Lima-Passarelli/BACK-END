Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

pessoasemcomida = 0

if Cr > Ca:
    pessoasemcomida += (Cr - Ca)
if Br > Ba:
    pessoasemcomida += (Br - Ba)
if Pr > Pa:
    pessoasemcomida += (Pr - Pa)

print(pessoasemcomida)
