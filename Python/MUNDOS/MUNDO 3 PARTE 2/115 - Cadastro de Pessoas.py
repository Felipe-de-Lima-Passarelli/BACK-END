from time import sleep

print(30*"-=")
print("                       MENU PRINCIPAL")
print(30*"-=")

escolha = int(input(f'''\033[1;33m1\033[m- \033[1;34mVer pessoas cadastradas\033[m
\033[1;33m2\033[m- \033[1;34mCadastrar nova Pessoa\033[m
\033[1;33m3\033[m- \033[1;34mSair do Sistema\033[m
{30*"-="}
\033[1;33mSua opção:\033[m '''))

while escolha != 1 and escolha != 2 and escolha != 3:
    print("\033[1;31mDigite uma opção válida, por favor\033[m")
    sleep(1)
    escolha = int(input(f'''\033[1;33m1\033[m- \033[1;34mVer pessoas cadastradas\033[m
\033[1;33m2\033[m- \033[1;34mCadastrar nova Pessoa\033[m
\033[1;33m3\033[m- \033[1;34mSair do Sistema\033[m
{30 * "-="}
\033[1;33mSua opção:\033[m '''))
    sleep(1)

while True:
    if escolha == 1:
        with open("Cadastros.txt", "r", encoding="utf-8") as arquivo1:
            conteudo = arquivo1.read()
            print(conteudo)
            sleep(1)
            escolha = int(input(f'''\033[1;33m1\033[m- \033[1;34mVer pessoas cadastradas\033[m
\033[1;33m2\033[m- \033[1;34mCadastrar nova Pessoa\033[m
\033[1;33m3\033[m- \033[1;34mSair do Sistema\033[m
{30 * "-="}
\033[1;33mSua opção:\033[m '''))
    elif escolha == 2:
        nome = str(input("Nome: "))
        idade = input("Idade: ")
        while not idade.isdigit() or int(idade) <= 0:
            print("Digite uma idade inteira válida")
            idade = input("Idade: ")
        idade = int(idade)
        with open("Cadastros.txt", "a", encoding = "utf-8") as arquivo2:
            arquivo2.write(f"\nNome: {nome} | Idade: {idade}")
        sleep(1)
        escolha = int(input(f'''\033[1;33m1\033[m- \033[1;34mVer pessoas cadastradas\033[m
\033[1;33m2\033[m- \033[1;34mCadastrar nova Pessoa\033[m
\033[1;33m3\033[m- \033[1;34mSair do Sistema\033[m
{30 * "-="}
\033[1;33mSua opção:\033[m '''))
    elif escolha == 3:
        print(30 * "\033[1;33m-=")
        print("               Saindo do Sistema... Até logo!")
        print(30 * "-=")
        print("\033[m")
        break
