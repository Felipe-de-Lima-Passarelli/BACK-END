tabela = ("Botafogo", "Fortaleza", "Palmeiras", "Flamengo", "Cruzeiro", "São Paulo", "Bahia", "Internacional", "Vasco", "Atlético-MG", "Bragantino", "Athletico-PR", "Juventude", "Criciúma", "Grêmio", "Fluminense", "Vitória", "Corinthians", "Cuiabá", "Atlético-GO")

print(f"Os primeiros cinco colocados do brasileirão são: {tabela[:5]}")
print(f"Os últimos quatro colocados do brasileirão são: {tabela[16:]}")
print(f"A ordem alfabética dos times do Brasileirão são: {sorted(tabela)}")
print(f"O Palmeiras está na {tabela.index("Palmeiras")+ 1}ª posição")
