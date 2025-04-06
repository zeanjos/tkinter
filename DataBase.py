import sqlite3
conexao = sqlite3.connect('Usuarios.db')

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
    
)
""")

conexao.close()

print('Conectado ao banco de dados')