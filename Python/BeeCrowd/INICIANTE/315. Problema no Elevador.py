f, s, g, u, d = map(int, input().split())

pressionar_botao = 0

if s < g:
    while s < g:
        s += u
        pressionar_botao += 1
    if s == g:
        print(pressionar_botao)
    else:
        s -= u #9
        pressionar_botao -= 1
        c = s + (u - d) #10
        pressionar_botao += 2
        if c <= s:
            print("use the stairs")
        else:
            s = c
            while s != g:
                c = s + (u - d)
                pressionar_botao += 2
            print(pressionar_botao)
else:
    if d == 0:
        print("use the stairs")
    else:
        while s > g:
            s -= d
            pressionar_botao += 1
        if s == g:
            print(pressionar_botao)
        else:
            s += d
            pressionar_botao -= 1
            c = s - (d - u)
            pressionar_botao += 2
            if c >= s:
                print("use the stairs")
            else:
                s = c
                while s != g:
                    c = s - (d - u)
                    pressionar_botao += 2
                    if c <= 0 or c > f:
                        print("use the stairs")
                        break
                    s = c
                else:
                    print(pressionar_botao)
