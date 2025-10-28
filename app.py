"""
Point d'entrée de l'application Flask e-commerce.
Crée une instance de l'application avec la configuration appropriée et la lance.
"""

from e_commerce import create_app
from config import Config


app = create_app(Config)

if __name__ == '__main__':
    app.run(debug=True)
