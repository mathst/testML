
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib
import sqlite3
import os

# Conecta ao banco SQLite e lê os dados
db_conn = sqlite3.connect('data/banco.db')
df = pd.read_sql_query("SELECT * FROM projetos", db_conn)

# Pré-processamento
le = LabelEncoder()
df['Recursos_Disponiveis'] = le.fit_transform(df['Recursos_Disponiveis'])

X = df[['Duracao', 'Orcamento', 'Tamanho_Equipe', 'Recursos_Disponiveis']]
y = df['Sucesso']

# Treinamento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliação
print(classification_report(y_test, model.predict(X_test)))

# Salva o modelo
joblib.dump(model, 'model/model_proj.pkl')

# Fecha conexão com o banco de dados
db_conn.close()