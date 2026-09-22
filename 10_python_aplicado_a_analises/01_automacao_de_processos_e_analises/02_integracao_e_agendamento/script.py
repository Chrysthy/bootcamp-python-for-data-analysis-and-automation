import requests

url = "https://api.agify.io/?name=ana"

resposta = requests.get(url)

dados = resposta.json()

print(dados)





import sqlite3

conn = sqlite3.connect("dados.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
nome TEXT,
idade INTEGER
)
""")

conn.commit()

print("Tabela criada com sucesso")





cursor.execute(
    "INSERT INTO usuarios VALUES (?,?)",
    ("Ana", 25)
)

conn.commit()

print("Usuário inserido no banco de dados")





cursor.execute("SELECT * FROM usuarios")

dados = cursor.fetchall()

print("Usuários no banco:")

for usuario in dados:
    print(usuario)






conn.close()

print("Conexão com o banco encerrada")