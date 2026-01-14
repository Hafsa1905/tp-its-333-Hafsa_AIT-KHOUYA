from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration de la base de données SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle de la table Personne
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Création de la base de données au démarrage
with app.app_context():
    db.create_all()

# 1. Page d'accueil simple (évite l'erreur TemplateNotFound)
@app.route('/')
def home():
    return "Service Personne (Port 5001) est en marche. Utilisez le Port 5000 pour l'interface."

# 2. API pour LIRE (utilisée par la Racine pour le tableau)
@app.route('/person_api', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    # On renvoie la liste au format JSON pour que le Port 5000 puisse la lire
    return jsonify([{"id": p.id, "name": p.name} for p in persons])

# 3. API pour AJOUTER (reçoit l'ordre du Port 5000)
@app.route('/add_api', methods=['POST'])
def add_api():
    name = request.form.get('name')
    if name:
        new_person = Person(name=name)
        db.session.add(new_person)
        db.session.commit()
        return jsonify({"message": "Succès"}), 200
    return jsonify({"error": "Nom manquant"}), 400

# 4. API pour SUPPRIMER (reçoit l'ordre du Port 5000)
@app.route('/delete_api/<int:id>', methods=['POST'])
def delete_api(id):
    person = Person.query.get(id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Supprimé"}), 200
    return jsonify({"error": "ID non trouvé"}), 404

if __name__ == '__main__':
    # Le service tourne sur le port 5001
    app.run(port=5001, debug=True)