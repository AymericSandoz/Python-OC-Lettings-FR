# Utilise une image de base légère avec Python 3.10
FROM python:3.10-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers de dépendances
COPY requirements.txt /app/

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste de l'application dans l'image
COPY . /app

# Définir des variables d'environnement (à adapter selon les besoins)
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=myapp.settings \
    PORT=8000

# Expose le port de l'application
EXPOSE 8000

# Commande pour lancer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
