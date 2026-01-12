from app import app
from flask import render_template, request, jsonify

### EXO1 - simple API
@app.route('/api/simple', methods=['GET'])
def simple_api():
    return jsonify({"message": "Ceci est une API en structure MVC"})
### EXO2 - API with simple display
### EXO2 - API with simple display
@app.route('/api/display', methods=['GET'])
def simple_display():
    # It will now look for the index.html you just created
    return render_template('index.html')
### EXO3 - API with parameters display 
@app.route('/api/parameters', methods=['GET'])
def parameters_display():
    # We define data here to send to the template
    user_name = "hafsa"
    return render_template('index.html', name=user_name)

### EXO4 - API with parameters retrieved from URL 
@app.route('/api/search', methods=['GET'])
def search_api():
    # On récupère la valeur du paramètre 'name' dans l'URL
    # Exemple: /api/search?name=Alice
    query_name = request.args.get('name', 'Utilisateur inconnu')
    
    return jsonify({
        "status": "success",
        "message": f"Bonjour {query_name}, votre paramètre a bien été récupéré !"
    })
