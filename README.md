# Projeto: Chatbot Inteligente para Previsão de Sucesso de Projetos

## 📅 Objetivo
Criar uma solução baseada em aprendizado de máquina que permita a previsão do sucesso de novos projetos, com base em dados históricos e no perfil do usuário que está submetendo o projeto. A solução inclui:

- Modelo de Machine Learning tradicional (Random Forest)
- API com Flask para previsões e consultas
- Chatbot interativo para coleta de dados e entrega de recomendação
- Base de dados SQLite para armazenamento

---

## 🔧 Componentes

### 1. `/model/` - Treinamento do Modelo
Contém o script `traning.py` que:
- Carrega dados do banco SQLite
- Preprocessa os dados
- Treina um modelo RandomForest
- Avalia e salva o modelo com `joblib`

> Execute com:
```bash
python model/traning.py
```

### 2. `/api/` - API Flask
Contém `app.py`, que:
- Exponibiliza a rota POST `/prever` para prever o sucesso de um projeto
- Exponibiliza GET `/user/<nome>` para buscar informações do usuário

> Inicie com:
```bash
python api/app.py
```

### 3. `/chatbot/` - Chatbot Terminal
Contém `chatbot.py`, que:
- Pergunta dados do projeto ao usuário
- Busca informações do usuário via API
- Envia dados para a API e exibe resultado

> Rode com:
```bash
python chatbot/chatbot.py
```

### 4. `/dados/` - Banco SQLite
Contém `init_db.py` para criar o banco `banco.db` com:
- Tabelas de projetos, usuários e previsões
- Dados de exemplo inseridos

> Inicialize com:
```bash
python dados/init_db.py
```
### 5. `main.py` - inicializador conjunto do projeto
Contém o script que:
- Inicia a API Flask
- Inicia o chatbot após a API estar pronta 
> Execute com:
```bash
python main.py
---

## 🔮 Abordagem Técnica

### Modelo de ML
- Escolhido: `RandomForestClassifier` por sua robustez e interpretabilidade
- Métricas usadas: `accuracy`, `precision`, `recall`, `f1-score`
- Preprocessamento: `LabelEncoder` para campos categóricos

### API
- Desenvolvida em Flask
- JSON como formato de entrada/saída
- Banco SQLite para consulta de usuários e salva de previsões

### Chatbot
- Simples (terminal) para prototipagem
- Busca perfil do usuário e adapta resposta

---

## 📄 Exemplos de uso

### Entrada JSON esperada para previsão:
```json
{
  "Duracao": 10,
  "Orcamento": 800000,
  "Tamanho_Equipe": 12,
  "Recursos_Disponiveis": 2
}
```

### Saída esperada da API:
```json
{
  "probabilidade_sucesso": 76.45
}
```

---

## ⚖️ Requisitos
- Python >= 3.8
- pandas
- scikit-learn
- flask
- requests
- joblib

Instale com:
```bash
pip install -r requirements.txt
```

---

## 📈 Melhorias Futuras
- Interface Web (ex.: Gradio, Streamlit)
- Autenticação de usuário
- Registro de histórico de previsões por usuário

---

## 🚀 Autores
- Desenvolvido por Matheus Teixeira

