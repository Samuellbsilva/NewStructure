from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/mensagem', methods=['POST'])
def mensagem():
    data = request.get_json()
    print("📥 Dados recebidos:", data)  # <-- Verifica se os dados chegaram

    if not data or 'nome' not in data:
        return jsonify({"erro": "Nome não fornecido"}), 400

    return jsonify({"mensagem": f"Olá, {data['nome']}! Bem-vindo à API Flask."})

if __name__ == '__main__':
    app.run(debug=True)
