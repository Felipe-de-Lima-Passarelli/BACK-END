# Importando as bibliotecas necessárias:
import pandas as pd
import pyodbc

# Importar o banco de dados:
tabela = pd.read_csv("Dados/cursos_com_id.csv")

# Criando a conexão com o Banco de Dados MySQL:
dados_conexao = (
   "Driver={MySQL ODBC 9.1 Unicode Driver};"
   "Server=localhost;"
   "Database=cadastro;"
   "UID=root;"
   "PWD=12345;"
)

# Criando e Inicializando o Cursor:
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Registrando todas vendas
for linha in tabela.index:
    comando = f"""INSERT INTO cursos (idcurso, nome, descricao, carga, totalaulas, ano)
    VALUES
    ({tabela.loc[linha, "idcurso"]}, "{tabela.loc[linha, "nome"]}", "{tabela.loc[linha, "descricao"]}", {tabela.loc[linha, "carga"]}, {tabela.loc[linha, "totalaulas"]}, {tabela.loc[linha, "ano"]})"""
    cursor.execute(comando)

#Finalizando o Programa
conexao.commit()
cursor.close()
conexao.close()
