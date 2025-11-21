#Passo 1 -> Importar as bibliotecas necessárias:
import pandas as pd
import pyodbc

#Passo 2 -> Importar o banco de dados:
tabela = pd.read_csv("Nome_Arquivo.csv")

#Passo 3 -> Criando a conexão com o Banco de Dados MySQL:
dados_conexao = (
   "Driver={MySQL ODBC 9.0 Unicode Driver};"
   "Server=localhost;"
   "Database=nome_do_banco_de_dados;"
   "UID=login;"
   "PWD=senha;"
)

#Passo 4 -> Criando e Inicializando o Cursor:
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

#Passo 5 -> Registrar o banco de dados:
#EXEMPLO DE TABELA:
 for linha in tabela.index:
    comando = f"""INSERT INTO Vendas (id_venda, cliente, produto, data_venda, preco, quantidade)
    VALUES
    ({tabela.loc[linha, "id_venda"]}, "{tabela.loc[linha, "cliente"]}", "{tabela.loc[linha, "produto"]}", "{tabela.loc[linha, "data_venda"]}", {tabela.loc[linha, "preco"]}, {tabela.loc[linha, "quantidade"]})"""
    cursor.execute(comando)

#Passo 6 -> Finalizando o Programa:
conexao.commit()
cursor.close()
conexao.close()
