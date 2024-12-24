# Importando as bibliotecas necessárias:
import pyodbc

# Criando a conexão com o Banco de Dados MySQL:
dados_conexao = (
   "Driver={MySQL ODBC 9.0 Unicode Driver};"
   "Server=localhost;"
   "Database=cadastro;"
   "UID=root;"
   "PWD=MySQL123!;"
)

# Criando e Inicializando o Cursor:
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Registrando um novo nome
comando = """update gafanhotos
set profissao = "Estudante"
where id = 2
"""
cursor.execute(comando)

#Finalizando o Programa
conexao.commit()
cursor.close()
conexao.close()
