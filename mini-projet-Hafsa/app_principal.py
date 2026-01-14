from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def dashboard():
    try:
        # 1. Récupère les noms (Port 5001)
        r_persons = requests.get('http://127.0.0.1:5001/person_api', timeout=2)
        persons = r_persons.json()
        
        # 2. Récupère la santé pour chaque ID (Port 5002)
        for p in persons:
            r_h = requests.get(f'http://127.0.0.1:5002/health/{p["id"]}', timeout=2)
            sante = r_h.json() if r_h.status_code == 200 else {}
            p['poids'] = sante.get('poids', 'N/A')
            p['taille'] = sante.get('taille', 'N/A')
                
        return render_template('index.html', data=persons)
    except Exception as e:
        return f"Erreur : Vérifiez les services 5001 et 5002 ! ({e})"

# Route pour AJOUTER (Envoie l'ordre au 5001)
@app.route('/add_person', methods=['POST'])
def add_person():
    nom = request.form.get('name')
    if nom:
        requests.post('http://127.0.0.1:5001/add_api', data={'name': nom})
    return redirect(url_for('dashboard'))

# Route pour SUPPRIMER (Envoie l'ordre au 5001)
@app.route('/delete_person/<int:id>')
def delete_person(id):
    requests.post(f'http://127.0.0.1:5001/delete_api/{id}')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)