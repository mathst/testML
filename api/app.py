from flask import Flask, request, jsonify
import joblib
import pandas as pd
import sqlite3

app = Flask(__name__)
modelo = joblib.load('model/model_proj.pkl')

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.get_json()
    df = pd.DataFrame([dados])
    result = modelo.predict_proba(df)[0][1]

    # Salvar projeto no banco
    conn = sqlite3.connect('data/banco.db')
    df['Sucesso_Previsto'] = result
    df.to_sql('projetos_novos', conn, if_exists='append', index=False)
    conn.close()

    return jsonify({'probabilidade_sucesso': round(result * 100, 2)})

@app.route('/user/<nome>', methods=['GET'])
def get_usuario(nome):
    conn = sqlite3.connect('data/banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE lower(nome)=?", (nome.lower(),))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "nome": row[1],
            "cargo": row[2],
            "historico": row[3],
            "experiencia": row[4],
            "sucesso_medio": row[5]
        })
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)