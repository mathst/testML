import requests
import sqlite3

print("\nBem-vindo ao Chatbot de Previsão de Sucesso de Projetos!")
print("Digite 'sair' para encerrar.")
# Conexão com o banco de dados
conn = sqlite3.connect('data/banco.db')
cursor = conn.cursor()
while True:
    # Verifica se o usuário já está cadastrado  
    nome = input("Qual seu nome? ").lower()
    resposta_usuario = requests.get(f"http://localhost:5000/user/{nome}")

    if resposta_usuario.status_code != 200:
        print("Usuário não encontrado. Vamos cadastrá-lo.")
        cargo = input("Cargo: ")
        historico = int(input("Histórico de projetos: "))
        experiencia = int(input("Experiência (anos): "))
        sucesso_medio = int(input("Sucesso médio (%): "))

        usuario_novo = {
            "nome": nome,
            "cargo": cargo,
            "historico": historico,
            "experiencia": experiencia,
            "sucesso_medio": sucesso_medio
        }
        requests.post("http://localhost:5000/user", json=usuario_novo)
        dados_usuario = usuario_novo# modificavel
    elif nome == "sair":
        print("Encerrando o chatbot. Até logo!")
        conn.close()
        break

    else:
        dados_usuario = resposta_usuario.json()
    
    print(f"\nOlá {dados_usuario['nome'].title()}! Vamos avaliar seu projeto.")
    print(f"Cargo: {dados_usuario['cargo']}")
    print(f"Experiência: {dados_usuario['experiencia']} anos")
    print(f"Sucesso médio: {dados_usuario['sucesso_medio']}%")
    print("Responda as perguntas a seguir para prever o sucesso do seu projeto:")
    duracao = int(input("Duração do projeto (quantidade de meses): "))
    orcamento = int(input("Orçamento do projeto (R$): "))
    equipe = int(input("Tamanho da equipe(quantidade de membros): "))
    recursos = input("Recursos (Alto/Médio/Baixo): ").capitalize()
    rec_map = {"Baixo": 0, "Médio": 1, "Alto": 2}

    entrada = {
        "Duracao": duracao,
        "Orcamento": orcamento,
        "Tamanho_Equipe": equipe,
        "Recursos_Disponiveis": rec_map.get(recursos, 1)
    }

    resposta = requests.post("http://localhost:5000/prever", json=entrada)
    probabilidade = resposta.json()["probabilidade_sucesso"]

    print(f"\n{nome.title()}, com base nos seus {dados_usuario['experiencia']} anos de experiência:")
    print(f"→ Chance de sucesso: {probabilidade}%")

    if probabilidade < 60:
        print("Projeto com baixa chance de sucesso. Considere rever orçamento/equipe.")
    else:
        print("Projeto com boas chances de sucesso!")
        
    print("\nDeseja avaliar outro projeto? (s/n)")
    continuar = input().lower()
    if continuar != 's':
        print("Encerrando o chatbot. Até logo!")
        conn.close()
        break
    else:
        print("Reiniciando o chatbot...")
        continue    