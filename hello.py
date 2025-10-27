from flask import Flask, request, jsonify
from supabase import create_client, Client

app = Flask(__name__)
SUPABASE_URL = "https://qhaanljyycfgwphxmqfq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFoYWFubGp5eWNmZ3dwaHhtcWZxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MTU5MTM5NiwiZXhwIjoyMDc3MTY3Mzk2fQ.1EtvtkqrYKqcdo1cn_Su1QenNO7tezWrAKh-9u21ymg"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/produits', methods=['GET'])
def get_produits():
    try:
        response = supabase.table("Articles").select("*").execute()
        print(response)  # 👈 Affiche la réponse brute dans la console
        return jsonify(response.data), 200
    except Exception as e:
        print("Erreur :", e)  # 👈 Affiche l'erreur dans le terminal
        return jsonify({"error": str(e)}), 500
