import json

# 1. Ouvrir data.json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Afficher chaque clé x valeur (pour le premier objet de "features")
print("--- Lecture des données ---")
feature = data["features"][0]
for cle, valeur in feature.items():
    print(f"{cle} : {valeur}")

# 3. MÀJ de la valeur de coordinates (ex: changer les coordonnées)
# On accède à la liste : [45.0, 5.1] et on modifie le premier élément
feature["geometry"]["coordinates"][0] = 48.85
feature["geometry"]["coordinates"][1] = 2.35
print("\n--- Coordonnées mises à jour ---")

# 4. Ajout d'un couple clé-valeur dans properties (prop1: true)
feature["properties"]["prop1"] = True
print("--- Propriété prop1 ajoutée ---")

# --- ÉTAPE FINALE : Sauvegarder les modifications dans le fichier ---
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
# Affichage formaté (comme sur ta capture d'écran)
print("\n--- Résultat Final Formaté ---")
print(json.dumps(data["features"], sort_keys=True, indent=4))