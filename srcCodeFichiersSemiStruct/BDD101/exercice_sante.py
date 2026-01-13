from flask import Flask, jsonify

app = Flask(__name__)

# 1. Base de données simulée avec plusieurs patients
# Note : Il y a deux "Hafsa", mais leurs ID sont uniques (1405 et 3000)
patients_db = [
    {
        "id": 1405,
        "nom": "Hafsa",
        "parametres_sante": {"GS": "A+", "maladie": "Aucune"}
    },
    {
        "id": 2002,
        "nom": "Marc",
        "parametres_sante": {"GS": "O-", "maladie": "Diabète"}
    },
    {
        "id": 3000,
        "nom": "Hafsa",
        "parametres_sante": {"GS": "B-", "maladie": "Grippe"}
    }
]

# 2. Route API avec ID et Paramètre choisi
@app.route('/sante/<int:patient_id>/<choix>', methods=['GET'])
def api_sante(patient_id, choix):
    # On cherche le patient qui possède l'ID indiqué dans l'URL
    patient_trouve = None
    for p in patients_db:
        if p["id"] == patient_id:
            patient_trouve = p
            break

    # Si l'ID n'existe pas dans notre liste
    if patient_trouve is None:
        return jsonify({"erreur": "Patient introuvable (ID incorrect)"}), 404

    # On extrait les données de santé pour ce patient précis
    sante = patient_trouve.get("parametres_sante", {})

    # Logique de sélection du paramètre
    if choix in sante:
        resultat = {choix: sante[choix]}
    elif choix in patient_trouve:
        resultat = {choix: patient_trouve[choix]}
    else:
        return jsonify({"erreur": f"Le paramètre '{choix}' n'existe pas pour ce patient"}), 404

    return jsonify(resultat)

if __name__ == '__main__':
    # Le serveur se lance sur le port 5000 par défaut
    app.run(debug=True)