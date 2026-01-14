# 1. Utiliser Python
FROM python:3.9-slim

# 2. Dossier de travail
WORKDIR /app

# 3. Copier les fichiers (app.py et data.json)
COPY . .

# 4. Installer uniquement Flask (pas besoin de SQLAlchemy ici car on utilise un JSON)
RUN pip install flask

# 5. Indiquer le port 5002 pour la santé
EXPOSE 5002

# 6. Lancer l'application
CMD ["python", "app.py"]