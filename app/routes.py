from flask import Blueprint, jsonify, request
from app.database import get_db
from app.auth import require_api_key

bp_routes = Blueprint('routes', __name__)

# ... (garde tes anciennes routes /api/v1/posts ici) ...

# ⚠️ AJOUTE BIEN CETTE ROUTE ICI :
@bp_routes.route('/api/gpt', methods=['GET'])
def ask_gpt():
    question = request.args.get('q', '').strip()

    if not question:
        return jsonify({'error': 'Le paramètre "q" est requis.'}), 400

    # Simulation de réponse (à remplacer par une vraie IA plus tard)
    if "école" in question.lower():
        reponse_ia = "L'école moderne a été influencée par Charlemagne, puis réformée par Jules Ferry."
    elif "qui es-tu" in question.lower():
        reponse_ia = "Je suis l'API de MotaDev sur Vercel !"
    else:
        reponse_ia = f"J'ai reçu votre question : '{question}'. L'IA arrive bientôt !"

    return jsonify({
        'question': question,
        'reply': reponse_ia
    })
    
