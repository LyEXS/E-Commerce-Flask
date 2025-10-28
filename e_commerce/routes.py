from flask import Blueprint, render_template, jsonify
from . import supabase

# Création d'un blueprint nommé 'main'
main = Blueprint('main', __name__)

# Définition de la route pour la page d'accueil
@main.route('/')
def home():
    """
    Page d'accueil — récupère les produits depuis Supabase et génère les URLs des images.
    """
    try:
        # Récupère tous les articles depuis la table 'Articles'
        response = supabase.table("Articles").select("*").execute()
        produits = response.data if hasattr(response, 'data') else []

        # Génère l'URL publique pour chaque article
        for p in produits:
            filename = p.get("image_path")
            if filename:
                # 🔹 Construire le lien vers le bucket public Supabase
                p["image_url"] = f"https://qhaanljyycfgwphxmqfq.supabase.co/storage/v1/object/public/Images/{filename}"
            else:
                p["image_url"] = "/static/images/placeholder.svg"  # fallback

        print("Articles pour la page d'accueil :", produits)  # 🔹 debug

    except Exception as e:
        print("Erreur lors de la récupération des produits :", e)
        produits = []

    # Passe les produits (avec image_url) au template
    return render_template('index.html', produits=produits)

@main.route('/articles', methods=['GET'])
def get_articles():
    try:
        response = supabase.table("Articles").select("*").execute()
        articles = response.data
        print("Articles bruts :", articles)

        # Pour chaque article, on génère le lien public
        for article in articles:
            image_path = article.get("image_path")
            if image_path:
                public_url = "https://qhaanljyycfgwphxmqfq.supabase.co/storage/v1/object/public/Images/{filename}"
                article["image_url"] = public_url
            else:
                article["image_url"] = "/static/default.jpg"  # image par défaut
        
        print("Articles récupérés :", articles)
   
        return jsonify(articles), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

