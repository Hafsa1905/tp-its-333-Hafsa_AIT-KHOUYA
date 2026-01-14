from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/health/<int:person_id>', methods=['GET'])
def get_health(person_id):
    file_path = 'data.json'
    if not os.path.exists(file_path):
        return jsonify({"poids": "N/A", "taille": "N/A"}), 200
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Recherche de l'ID dans le fichier JSON
    result = next((item for item in data if item["id_personne"] == person_id), None)
    
    if result:
        return jsonify(result)
    return jsonify({"poids": "N/A", "taille": "N/A"}), 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)