from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # 1. On récupère les noms depuis le port 5001
        r_pers = requests.get('http://127.0.0.1:5001/person_api')
        persons = r_pers.json()

        final_list = []
        for p in persons:
            # 2. Pour chaque ID, on demande la santé au port 5002
            r_health = requests.get(f'http://127.0.0.1:5002/health/{p["id"]}')
            health_data = r_health.json() if r_health.status_code == 200 else {}
            
            final_list.append({
                "id": p["id"],
                "name": p["name"],
                "poids": health_data.get("poids", "N/A"),
                "taille": health_data.get("taille", "N/A")
            })
        return render_template('index.html', data=final_list)
    except:
        return "Erreur : Lancez les services 5001 et 5002 d'abord !"

if __name__ == '__main__':
    app.run(port=5000, debug=True)