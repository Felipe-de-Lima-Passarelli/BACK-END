from time import sleep

while True:
    print("\033[1;97;32m",40*"-=")
    print("SISTEMA DE AJUDA PyHELP")
    print(40 * "-=")
    x = str(input("\033[m""Digite o comando que deseja conhecer melhor as informações: "))
    sleep(1)
    if x.strip().lower() == "fim":
        break
    print("\033[1;97;44m",20 * "-=")
    print(f"Acessando o manual do comando {x}")
    print(20 * "-=")
    sleep(1)
    print("\033[7;97;40m)")
    help(x)

print("\033[1;97;41m",20*"-=")
print("                 Até logo")
print(20*"-=")
