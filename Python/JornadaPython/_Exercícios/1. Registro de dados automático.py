# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login.
# Passo 3: Importar a base de dados.
# Passo 4: Cadastrar todos produtos.

import pandas
import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("op")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
sleep(1)

pyautogui.click(x=902, y=389)
pyautogui.write("email_ficticio@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha_ficticia")
pyautogui.click(x=981, y=556)
sleep(0.5)

tabela = pandas.read_csv("Dados/Produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=745, y=275)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(1000)
    else:
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(1000)

print("Fim do Programa")
