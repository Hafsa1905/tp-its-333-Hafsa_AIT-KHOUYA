# 1. Utiliser une image Python officielle
FROM python:3.9-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier les fichiers de ton service dans le conteneur
COPY . .

# 4. Installer Flask et SQLAlchemy (les bibliothèques dont on a besoin)
RUN pip install flask flask-sqlalchemy

# 5. Indiquer que le service utilise le port 5001
EXPOSE 5001

# 6. Lancer l'application
CMD ["python", "app.py"]