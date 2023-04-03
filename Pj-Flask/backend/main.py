from flask import Flask, jsonify, request
from flask_cors import CORS
from functions import *
from messages import *
app = Flask(__name__)
CORS(app)

# Rota para listar todos os itens
@app.route('/itens', methods=['GET'])
def get_itens():
    return jsonify(itens)

# Rota para buscar um item por ID
@app.route('/itens/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in itens:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'message': 'Item não encontrado'})

# Rota para adicionar um novo item
@app.route('/sample', methods=['POST'])
def add_item():
    mp10 = request.json['mp10']
    mp25 = request.json['mp25']
    o3 = request.json['o3']
    co = request.json['co']
    no2 = request.json['no2']
    so2 = request.json['so2']
    print (mp10, mp25, o3, co, no2, so2)
    return jsonify({"status":200})

# Rota para atualizar um item existente
@app.route('/itens/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    for item in itens:
        if item['id'] == item_id:
            item['nome'] = request.json['nome']
            return jsonify(item)
    return jsonify({'message': 'Item não encontrado'})

# Rota para excluir um item existente
@app.route('/itens/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in itens:
        if item['id'] == item_id:
            itens.remove(item)
            return jsonify({'message': 'Item excluído com sucesso'})
    return jsonify({'message': 'Item não encontrado'})

if __name__ == '__main__':
    app.run(debug=True)
