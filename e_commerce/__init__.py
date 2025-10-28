
"""
Initialise et configure l'application Flask.

Cette fonction factory crée une nouvelle instance de l'application Flask avec la configuration suivante :
- Charge la configuration depuis l'objet de configuration fourni
- Initialise la connexion Supabase
- Enregistre le blueprint principal contenant les routes de l'application

Returns:
    Flask: Une instance d'application Flask configurée et prête à traiter les requêtes
"""

from flask import Flask
from supabase import create_client, Client

# Variable globale pour stocker l'instance du client Supabase
supabase: Client = None

def create_app(config_class):
    # Crée l'application Flask
    app = Flask(__name__)
    
    # Charge la configuration
    app.config.from_object(config_class)
    
    # Initialise le client Supabase
    global supabase
    supabase = create_client(
        app.config['SUPABASE_URL'],
        app.config['SUPABASE_KEY']
    )

    # Importation et enregistrement du blueprint principal
    from .routes import main
    app.register_blueprint(main)

    return app

