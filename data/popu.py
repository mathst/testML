import sqlite3
import random

# Função para gerar dados aleatórios
def gerar_dados_projetos(qtd=100):
    dados = []
    for _ in range(qtd):
        duracao = random.randint(2, 24)
        orcamento = random.randint(100000, 3000000)
        tamanho_equipe = random.randint(3, 30)
        recursos_disponiveis = random.choice(["Baixo", "Médio", "Alto"])
        
        score = (
            (duracao <= 18) +
            (orcamento >= 500000) +
            (tamanho_equipe >= 10) +
            (recursos_disponiveis == "Alto") * 2 +
            (recursos_disponiveis == "Médio")
        )
        sucesso = 1 if score >= 3 else 0

        dados.append((duracao, orcamento, tamanho_equipe, recursos_disponiveis, sucesso))
    return dados

# Conexão e criação do banco
conn = sqlite3.connect('data/banco.db')
c = conn.cursor()

# Criação da tabela
c.execute('''
CREATE TABLE IF NOT EXISTS projetos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Duracao INTEGER,
    Orcamento INTEGER,
    Tamanho_Equipe INTEGER,
    Recursos_Disponiveis TEXT,
    Sucesso INTEGER
)
''')

# Geração dos dados
projetos = gerar_dados_projetos(100)

# Inserção dos dados
c.executemany('''
INSERT INTO projetos (Duracao, Orcamento, Tamanho_Equipe, Recursos_Disponiveis, Sucesso)
VALUES (?, ?, ?, ?, ?)
''', projetos)

# Confirma a inserção
conn.commit()

# Verificar se os dados foram inseridos
c.execute("SELECT COUNT(*) FROM projetos")
quantidade = c.fetchone()[0]
print(f"Total de projetos inseridos no banco: {quantidade}")

# Exemplo: mostrar os 5 primeiros
c.execute("SELECT * FROM projetos LIMIT 5")
for linha in c.fetchall():
    print(linha)

# Encerrar conexão
conn.close()
