pessoastotal = []
pessoasvolta = 0
contagem = 0

while True:
    dados = input().split()
    if len(dados) == 2:
        caminho = str(dados[0])
        T = int(dados[1])
    else:
        caminho = str(dados[0])
        T = 0

    if caminho == "ABEND":
        break

    if caminho == "SALIDA":
        pessoastotal.append(T)
    else:
        pessoasvolta += T
        contagem += 1

resultado = sum(pessoastotal) - pessoasvolta
print(resultado)
print(len(pessoastotal) - contagem)
