def remover_pessoa(nome_remover):
    with open("dados.csv", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    linhas_atualizadas = [linhanova for linhanova in linhas if nome_remover not in linhanova]

    with open("dados_atualizados.csv", "w", encoding="utf-8") as arquivo_atualizado:
        arquivo_atualizado.writelines(linhas_atualizadas)

remover_pessoa("Felipe")

print(15*"-=")
print("       Fim do Programa!")
print(15*"-=")
