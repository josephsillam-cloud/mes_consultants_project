Projet Django minimal généré automatiquement.

Nom du projet: mes_consultants
Base de données: SQLite3

Instructions rapides:
1. Crée un environnement virtuel et active-le.
   python -m venv .venv
   source .venv/bin/activate   (Linux / macOS)
   .venv\Scripts\activate     (Windows PowerShell)

2. Installe Django:
   pip install django

3. Place-toi à la racine du projet (le dossier contenant manage.py) et lance:
   python manage.py makemigrations
   python manage.py migrate

4. Charge les fixtures:
   python manage.py loaddata consultants/fixtures/consultants_fixture.json
   # ou: python manage.py populate_consultants

5. Crée un superuser si tu veux accéder à l'admin:
   python manage.py createsuperuser

6. Lance le serveur:
   python manage.py runserver

Notes:
- Le SECRET_KEY dans settings.py est un placeholder: remplace-le pour la production.
- DEBUG=True pour faciliter le démarrage; change-le en production.
