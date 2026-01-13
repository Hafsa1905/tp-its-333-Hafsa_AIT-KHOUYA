from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import app
import sqlite3

# --- 1. CONFIGURATION SQLALCHEMY (Image 15) ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- 2. MODELES POUR L'EXERCICE (Images 15 & 17) ---
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # Relation un-à-plusieurs (Image 17)
    etudiants = db.relationship('Etudiant', backref='group', lazy=True)

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), unique=True, nullable=False)
    adresse = db.Column(db.String(120), unique=True, nullable=False)
    pin = db.Column(db.String(20), unique=True, nullable=False)
    # Clé étrangère (Image 17)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)

# --- 3. ROUTES ---

# Affiche ton formulaire HTML
@app.route('/ajout')
def index():
    return render_template('index.html')

# # Route pour l'exercice SQLAlchemy (Images 16 & 17)
# @app.route('/exercice_alchemy')
# def exercice_alchemy():
#     db.create_all() # Crée test.db (Image 16)
    
#     # On crée le groupe ITS2 s'il n'existe pas
#     if not Group.query.filter_by(name='ITS2').first():
#         its2 = Group(name="ITS2")
#         db.session.add(its2)
        
#         # Création des 3 étudiants (Image 17)
#         john = Etudiant(nom='john', adresse='122 rue paul armangot', pin='123', group=its2)
#         hafsa = Etudiant(nom='hafsa', adresse='rue de paris', pin='456', group=its2)
#         lucas = Etudiant(nom='lucas', adresse='avenue des champs', pin='789', group=its2)
        
#         db.session.add_all([john, hafsa, lucas])
#         db.session.commit() # Valide (Image 16)
#         return "Succès : Groupe ITS2 et 3 étudiants créés !"
#     return "L'exercice a déjà été exécuté."

# # Route pour ton formulaire (Action du bouton Send)
# @app.route('/add', methods=['POST'])
# def add_patient():
#     # Récupération des données du formulaire
#     nom = request.form['n']
#     adresse = request.form['add']
#     pin = request.form['pin']
#     gs = request.form['gs']
#     maladie = request.form['maladie']

#     # Ici, tu peux garder ton ancienne logique sqlite3 pour database.db
#     with sqlite3.connect("database.db") as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO patients (nom, adresse, pin, gs, maladie) VALUES (?,?,?,?,?)", 
#                     (nom, adresse, pin, gs, maladie))
#         con.commit()
    
#     return "Patient ajouté avec succès dans database.db !"