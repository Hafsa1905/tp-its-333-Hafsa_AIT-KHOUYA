from flask import render_template, request, jsonify
import sqlite3

# Import de 'app' à la fin du fichier ou utilisation directe
from app import app 

# --- FONCTION DE CONNEXION ---
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    return conn

# --- ROUTES ---

# 1. Affiche le formulaire sur localhost:5000/ajout
@app.route('/ajout')
def new_student():
    return render_template('index.html')

# 2. Reçoit les données du bouton "Send"
@app.route('/add', methods=['POST'])
def add_record():
    if request.method == 'POST':
        try:
            nm = request.form['n']
            ad = request.form['add']
            pn = request.form['pin']
            gs = request.form['gs']
            mal = request.form['maladie']

            with get_db_connection() as con:
                cur = con.cursor()
                cur.execute("INSERT INTO etudiants (nom, addr, pin, gs, maladie) VALUES (?,?,?,?,?)", 
                            (nm, ad, pn, gs, mal))
                con.commit()
                msg = "Enregistrement réussi !"
        except Exception as e:
            msg = f"Erreur lors de l'insertion : {e}"
        finally:
            return msg

# 3. Route pour consulter les données (ex: /sante/1/maladie)
@app.route('/sante/<int:patient_id>/<choix>')
def consulter_sante(patient_id, choix):
    con = get_db_connection()
    patient = con.execute('SELECT * FROM etudiants WHERE id = ?', (patient_id,)).fetchone()
    con.close()

    if patient is None:
        return jsonify({"erreur": "Patient introuvable"}), 404

    if choix in patient.keys():
        return jsonify({choix: patient[choix]})
    else:
        return jsonify({"erreur": "Paramètre inconnu"}), 404