import sqlite3

conn = sqlite3.connect('data/banco.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS projetos (
    Projeto_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Duracao INTEGER,
    Orcamento INTEGER,
    Tamanho_Equipe INTEGER,
    Recursos_Disponiveis TEXT,
    Sucesso INTEGER
)''')

c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    Usuario_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cargo TEXT,
    historico INTEGER,
    experiencia INTEGER,
    sucesso_medio INTEGER
)''')

c.execute('''CREATE TABLE IF NOT EXISTS projetos_novos (
    Duracao INTEGER,
    Orcamento INTEGER,
    Tamanho_Equipe INTEGER,
    Recursos_Disponiveis INTEGER,
    Sucesso_Previsto REAL
)''')

# Inserção de dados exemplo
usuarios = [
    ("joao", "Gerente de TI", 15, 5, 80),
    ("maria", "Analista de Projetos", 10, 3, 65),
    ("pedro", "Coordenador de Projetos", 25, 8, 90)
]

c.executemany("INSERT INTO usuarios (nome, cargo, historico, experiencia, sucesso_medio) VALUES (?, ?, ?, ?, ?)", usuarios)

projetos = [
    (6, 500000, 10, "Alto", 1),
    (12, 1000000, 15, "Médio", 0),
    (9, 750000, 8, "Baixo", 1),
    (18, 2000000, 20, "Alto", 1)
]

c.executemany("INSERT INTO projetos (Duracao, Orcamento, Tamanho_Equipe, Recursos_Disponiveis, Sucesso) VALUES (?, ?, ?, ?, ?)", projetos)

conn.commit()
conn.close()
# Fechando a conexão com o banco de dados