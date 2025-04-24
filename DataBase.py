import sqlite3

database = sqlite3.connect('primeiro_banco.db')
cursor = database.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cadastro (
    numero INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL
    senha INTEGER NOT NULL
    email TEXT NOT NULL,
    telefone INTEGER NOT NULL
)
''')

def insert_date(usuario, senha, email, telefone):
    cursor.execute("INSERT INTO cadastro (usuario, senha, email, telefone) VALUES(?, ?, ?, ?)", (usuario, senha, email, telefone))
    database.commit()
    database.close()
print('Conectado ao banco de dados')