from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/health/<int:person_id>', methods=['GET'])
def get_health(person_id):
    if not os.path.exists('data.json'):
        return jsonify({"error": "Fichier non trouve"}), 404
    with open('data.json', 'r') as f:
        data = json.load(f)
    # On cherche les infos santé correspondant à l'ID
    result = next((item for item in data if item["id_personne"] == person_id), None)
    if result:
        return jsonify(result)
    return jsonify({"error": "ID inconnu"}), 404

if __name__ == '__main__':
    app.run(port=5002, debug=True)